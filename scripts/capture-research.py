from pathlib import Path
import subprocess,json,sys
ROOT=Path(__file__).resolve().parents[1]
sites=[('skinspirit','https://www.skinspirit.com'),('everbody','https://everbody.com'),('alchemy43','https://alchemy43.com'),('ject','https://ject.us'),('heyday','https://www.heydayskincare.com'),('thethingswedo','https://thethingswedo.co'),('curated-medical','https://curatedmed.com'),('inside-out','https://insideoutaesthetics.com'),('the-comstock','https://thecomstock.com'),('institute-of-aesthetics','https://www.instituteofaesthetics.com')]
def cli(*args):
 r=subprocess.run(['playwright-cli','-s=velmora-research','--raw',*args],cwd=ROOT,text=True,capture_output=True,timeout=150)
 if r.returncode: raise RuntimeError(r.stdout+r.stderr)
 return r.stdout.strip()
for n,(slug,url) in enumerate(sites,1):
 if len(sys.argv)>1 and n not in [int(x) for x in sys.argv[1:]]: continue
 dest=ROOT/'research/sites'/f'{n:02}-{slug}';dest.mkdir(parents=True,exist_ok=True);(dest/'images').mkdir(exist_ok=True)
 print('START',slug,flush=True)
 try:
  cli('open')
  code=r'''async page => {
const network=[];page.on('request',r=>network.push(r.method()+' '+r.url()));
await page.setViewportSize({width:1440,height:900}); await page.goto(URL,{waitUntil:'domcontentloaded',timeout:60000}); await page.waitForTimeout(3500);
for(const pattern of [/deny non-essential/i,/reject all/i,/decline/i,/close popup/i,/close dialog/i]) { const b=page.getByRole('button',{name:pattern}).first();if(await b.isVisible().catch(()=>false))await b.click().catch(()=>{}); }
for(const sel of ['.spu-close','.pum-close','.dialog-close-button','.osano-cm-deny','[aria-label="Close"]','button[aria-label*="Close popup"]']){const b=page.locator(sel).first();if(await b.isVisible().catch(()=>false))await b.click({timeout:1500}).catch(()=>{});} await page.waitForTimeout(500);
await page.screenshot({path:DEST+'/hero-desktop.png'});
const scroll=async()=>{for(let y=0;y<Math.min(await page.evaluate(()=>document.body.scrollHeight),22000);y+=650){await page.evaluate(y=>window.scrollTo(0,y),y);await page.waitForTimeout(100);}await page.evaluate(()=>window.scrollTo(0,0));await page.waitForTimeout(400);};
await scroll();await page.screenshot({path:DEST+'/desktop-full.png',fullPage:true});
const data=await page.evaluate(()=>{const style={};for(const [key,sel]of Object.entries({h1:'h1',h2:'h2',body:'body',nav:'nav a,header a',button:'a[class*=button],button'})){let el=document.querySelector(sel);if(el){let s=getComputedStyle(el);style[key]={text:el.textContent.trim().slice(0,120),font:s.fontFamily,size:s.fontSize,color:s.color,background:s.backgroundColor,spacing:s.letterSpacing};}}return {title:document.title,html:document.documentElement.outerHTML,styles:style,text:document.body.innerText,images:[...new Set([...document.images].filter(i=>i.naturalWidth>200).map(i=>i.currentSrc||i.src))].slice(0,20),links:[...document.querySelectorAll('a[href]')].map(a=>({text:a.innerText.trim(),href:a.href})).filter(a=>a.text&&a.href.startsWith(location.origin))};});
await page.setViewportSize({width:390,height:844});await page.reload({waitUntil:'domcontentloaded'});await page.waitForTimeout(2000);for(const sel of ['.spu-close','.pum-close','.dialog-close-button','.osano-cm-deny','[aria-label="Close"]']){const b=page.locator(sel).first();if(await b.isVisible().catch(()=>false))await b.click({timeout:1500}).catch(()=>{});}await scroll();await page.screenshot({path:DEST+'/mobile-full.png',fullPage:true});
const candidates=page.locator('button,[role=button],a[aria-label],summary');let menu=null;
for(let i=0;i<await candidates.count();i++){const e=candidates.nth(i);const info=await e.evaluate(e=>[e.getAttribute('aria-label'),e.className,e.id,e.textContent.slice(0,50)].join(' '));if(/menu|hamburger|nav-toggle|mobile-toggle/i.test(info)&&!/accessibility|cookie/i.test(info)&&await e.isVisible()){await e.click({timeout:2500}).catch(()=>{});menu=info;break;}}
await page.waitForTimeout(500);await page.screenshot({path:DEST+'/nav-open-mobile.png'});data.menu=menu;
const link=data.links.find(l=>/botox|injectable|facial|treatment|service/i.test(l.text)&&l.href.replace(/\/$/,'')!==URL.replace(/\/$/,'')&&!l.href.includes('#'))||data.links.find(l=>/about|story/i.test(l.text));
if(link){await page.setViewportSize({width:1440,height:900});await page.goto(link.href,{waitUntil:'domcontentloaded',timeout:60000});await page.waitForTimeout(2000);await scroll();await page.screenshot({path:DEST+'/inner-page.png',fullPage:true});data.inner={url:page.url(),title:await page.title(),html:await page.content()};}
data.network=network;return data;
}'''.replace('URL',json.dumps(url)).replace('DEST',json.dumps(str(dest)))
  result=cli('run-code',code);data=json.loads(result)
  (dest/'page.html').write_text(data.pop('html'))
  (dest/'styles.json').write_text(json.dumps(data.pop('styles'),indent=2))
  network=data.pop('network');(dest/'network.txt').write_text('\n'.join(network)+'\n\nMOTION/MEDIA MATCHES:\n'+'\n'.join(x for x in network if any(k in x.lower() for k in ['three','spline','gsap','lenis','.mp4','.webm','video'])))
  if 'inner'in data:(dest/'inner-page.html').write_text(data['inner'].pop('html'))
  (dest/'capture.json').write_text(json.dumps(data,indent=2))
  downloaded=[]
  for u in data['images']:
   f=dest/'images'/f'reference-{len(downloaded)+1:02}.img'
   r=subprocess.run(['curl','-L','--fail','--max-time','20','-s',u,'-o',str(f)])
   if r.returncode==0 and f.exists() and f.stat().st_size>1000:downloaded.append(u)
   elif f.exists():f.unlink()
   if len(downloaded)>=7:break
  (dest/'images/sources.json').write_text(json.dumps(downloaded,indent=2))
  print('DONE',slug,'images',len(downloaded),'menu',data.get('menu'),'inner',data.get('inner'),flush=True)
 except Exception as e: print('ERROR',slug,str(e)[:1200],flush=True);(dest/'capture-error.txt').write_text(str(e))
 finally:
  try:cli('close')
  except:pass
