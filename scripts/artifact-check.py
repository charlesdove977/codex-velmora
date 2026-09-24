from pathlib import Path
import json,hashlib,re,gzip
root=Path('.')
required=['desktop-full.png','mobile-full.png','hero-desktop.png','nav-open-mobile.png','page.html','styles.json','network.txt','notes.md','inner-page.png','inner-page.html']
research=[]
for folder in sorted(Path('research/sites').iterdir()):
 if folder.is_dir():research.append({'folder':folder.name,'missing':[n for n in required if not (folder/n).is_file() or not (folder/n).stat().st_size], 'images':len(list((folder/'images').glob('*.img')))})
hashes={hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('research/sites').rglob('*') if p.is_file()}
shared=[str(p) for d in ['src','public'] for p in Path(d).rglob('*') if p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() in hashes]
credits=Path('CREDITS.md').read_text();families=sorted(set(re.sub(r'-\d+\.(avif|webp)$','',p.name) for p in Path('public/images').glob('*') if re.search(r'-\d+\.(avif|webp)$',p.name)))
images=[{'family':f,'credited':f+'-' in credits,'variants':len([p for p in Path('public/images').glob(f+'-*') if re.search(r'-(480|960|1600)\.(avif|webp)$',p.name)])} for f in families]
banned=[str(p) for p in Path('src').rglob('*') if p.is_file() and re.search('lorem|todo|placeholder|tbd',p.read_text(),re.I)]
chunks=[{'file':p.name,'gzipBytes':len(gzip.compress(p.read_bytes()))} for p in Path('dist/client/_astro').glob('GlassCanvas*.js')]
result={'research':research,'researchFilesShipped':shared,'stockImages':images,'unfinishedCopyMatches':banned,'threeChunks':chunks}
Path('verification/artifact-check.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
assert len(research)==10 and all(not x['missing'] and 5<=x['images']<=10 for x in research)
assert not shared and not banned and all(x['credited'] and x['variants']==6 for x in images)
