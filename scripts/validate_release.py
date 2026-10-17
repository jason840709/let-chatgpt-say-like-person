#!/usr/bin/env python3
"""Validate local release sources and built assets without network or installation."""
from pathlib import Path
import ast, hashlib, json, re, zipfile
ROOT = Path(__file__).resolve().parents[1]
script = ast.parse((ROOT/'scripts/build_release.py').read_text())
names = next(ast.literal_eval(n.value) for n in script.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='NAMES' for t in n.targets))
manifest = json.loads((ROOT/'dist/package-manifest.json').read_text())
archive = ROOT/'dist'/('let-chatgpt-say-like-person-v'+manifest['version']+'.zip')
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(manifest['files'])
    for name, meta in manifest['files'].items():
        source=(ROOT/name).read_bytes()
        assert z.read('let-chatgpt-say-like-person/'+name)==source
        assert hashlib.sha256(source).hexdigest()==meta['sha256']
    assert not any('.DS_Store' in n or '__MACOSX' in n for n in z.namelist())
assert re.search(r'^name: let-chatgpt-say-like-person$',(ROOT/'SKILL.md').read_text(),re.M)
missing=[]
for f in [ROOT/name for name in manifest['files'] if name.endswith('.md')]:
    text=f.read_text()
    assert not any(x in text for x in ['/Users/','/Volumes/','/private/','github_pat_','ghp_'])
    for match in re.finditer(r'\]\(([^)]+)\)',text):
        target=match.group(1).split('#',1)[0]
        if target and not target.startswith(('https:','http:','mailto:')) and not (f.parent/target).exists():
            missing.append((str(f.relative_to(ROOT)),target))
assert not missing, missing
page=(ROOT/'index.html').read_text()
data=json.loads(re.search(r'<script type="application/json" id="sources">(.*?)</script>',page,re.S).group(1))
assert all(data['doc-'+str(i)]==(ROOT/name).read_text() for i,(name,_) in enumerate(names))
assert 'VERSION '+manifest['version'] in page
assert '/download/v'+manifest['version']+'/' in page
print(json.dumps({'version':manifest['version'],'zip_members':len(manifest['files']),'zip_matches_sources':True,'relative_links_missing':missing,'offline_embedded_sources':len(names),'public_name_preserved':True,'macos_junk_excluded':True,'local_path_scan_passed':True},ensure_ascii=False))
