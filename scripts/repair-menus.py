from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parents[1]
for slug,url,selector in [('04-ject','https://ject.us','.mobile-trigger-new'),('06-thethingswedo','https://thethingswedo.co','.js-drawer-open-button-left'),('07-curated-medical','https://curatedmed.com','.e-n-menu-toggle')]:
 dest=str(root/'research/sites'/slug)
 code='''async page => {await page.setViewportSize({width:390,height:844});await page.goto(URL,{waitUntil:'domcontentloaded'});await page.waitForTimeout(3500);const e=page.locator(SEL+':visible').first();await e.click({timeout:4000});await page.waitForTimeout(700);await page.screenshot({path:DEST+'/nav-open-mobile.png'});return {menu:SEL,expanded:await e.getAttribute('aria-expanded'),text:(await page.locator('body').innerText()).slice(0,700)};}'''.replace('URL',json.dumps(url)).replace('SEL',json.dumps(selector)).replace('DEST',json.dumps(dest))
 r=subprocess.run(['playwright-cli','-s=velmora-repair','--raw','run-code',code],capture_output=True,text=True,cwd=root)
 (Path(dest)/'menu-repair.json').write_text(r.stdout);print(slug,r.stdout[:800],flush=True)
subprocess.run(['playwright-cli','-s=velmora-repair','close'],cwd=root)
