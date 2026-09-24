from pathlib import Path
import json
root=Path('.')
def result(name):
 s=(root/'verification'/name).read_text();assert s.startswith('### Result'),name+' has no successful result';return json.loads(s.split('### Result\n')[1].split('\n')[0])
a=result('page-audit-final.txt');assert len(a)==165;assert all(not x['overflow'] and not x['brokenImages'] and x['h1']==1 and (not x['errors'] or x['status']==404) for x in a)
meta=result('metadata-check.txt');assert len(meta)==51 and all(x['status']==200 and x['description'] and x['canonical'] and x['og'] and not x['missingAlt'] and not x['emptyLinks'] for x in meta)
assert all(x['passed'] for x in result('booking-check.txt'))
for f in ['forms-check.txt','forms-desktop-check.txt']:assert len(result(f))==4 and all(x['invalid'] and x['success'] for x in result(f))
for f in ['api-negative.json','email-check.json']:assert all(x['passed'] for x in json.loads((root/'verification'/f).read_text()))
motion=result('motion-check.txt');assert not motion['errors'] and motion['hero']['visible'] and all(x['canvas'] and len(x['visible'])==1 for x in motion['method']) and motion['reduced']=={'canvas':0,'poster':True} and motion['mobile']['steps']==4
ui=result('final-ui-check.txt');assert all(not x['overflow'] for x in ui['pages']) and ui['policySearch'] and ui['mapPanel'] and ui['mapLoaded'] and ui['tabs']=='true' and ui['noWebGL']=={'canvas':0,'poster':True}
for name in ['home','treatment']:
 d=json.loads((root/'verification'/f'lighthouse-{name}-final.report.json').read_text())['categories'];assert d['performance']['score']>=.85 and d['accessibility']['score']>=.95 and d['best-practices']['score']>=.95 and d['seo']['score']==1
assert json.loads(Path('verification/dependency-audit-final.json').read_text())['metadata']['vulnerabilities']['total']==0
assert len(list(Path('verification/pages').glob('*.png')))==110
for p in Path('.paul/phases').glob('*/*-PLAN.md'):assert p.with_name(p.name.replace('-PLAN','-SUMMARY')).exists()
for p in ['README.md','CREDITS.md','verification/ACCEPTANCE.md','verification/VISUAL-REVIEW.md','research/SITES.md','research/ELEMENTS.md']:
 assert Path(p).stat().st_size>0
assert '0 errors' in Path('verification/final-build.log').read_text()
assert not json.loads(Path('verification/brand-render-check.json').read_text())['unexpectedCurrencyPrefix']
assert json.loads(Path('verification/three-budget.json').read_text())['totalGzipBytes']<260000
out={'passed':True,'routeViewportChecks':165,'sitemapRoutes':51,'pageScreenshots':110,'paulLoops':4,'evidence':'See ACCEPTANCE.md for item-level evidence, manual review and deliberate demo boundaries.'}
Path('verification/completion-audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
