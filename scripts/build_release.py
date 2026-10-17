#!/usr/bin/env python3
"""Build the ZIP and a source-derived offline reader; never edit installed skills."""
from pathlib import Path
import hashlib, html, json, re, zipfile
import markdown

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT
SKILL_NAME = 'let-chatgpt-say-like-person'
DIST = ROOT / 'dist'
DIST.mkdir(exist_ok=True)
VERSION = '2.8.1'
NAMES = [
 ('SKILL.md','核心原則與檢查'),
 ('references/reader-and-referents.md','讀者與方法解釋'),
 ('references/numbers-and-statistics.md','數字與研究方法'),
 ('references/claims-and-hedging.md','證據與必要限制'),
 ('references/conversation-and-ui.md','對話與介面'),
 ('references/natural-zh-tw.md','自然繁體中文'),
 ('references/documents.md','文件與圖表'),
 ('references/review-gates.md','完整審查'),
 ('README.md','使用說明'),
 ('CHANGELOG.md','修改紀錄'),
 ('VALIDATION.md','驗證範圍'),
 ('docs/upgrade-v2.6.0-to-v2.8.1.md','從2.6.0升級'),
 ('docs/validation-v2.6.0.md','2.6.0歷史驗證'),
]
ids = {name:f'doc-{i}' for i,(name,_) in enumerate(NAMES)}
texts = {}
articles = []
nav = []
for i,(name,label) in enumerate(NAMES):
    source = (SKILL/name).read_text()
    texts[ids[name]] = source
    body = re.sub(r'\A---\n.*?\n---\n','',source,count=1,flags=re.S)
    rendered = markdown.markdown(body,extensions=['tables','fenced_code','toc'])
    # Make headings unique across separately rendered documents.
    rendered = re.sub(r'id="([^"]+)"',lambda m:f'id="{ids[name]}-{m[1]}"',rendered)
    def fix_link(m):
        target = m[1]
        if target.startswith('#'):
            return f'href="#{ids[name]}-{target[1:]}"'
        import posixpath
        local = posixpath.normpath((Path(name).parent/target).as_posix())
        if local.startswith('references/../'):
            local = local[len('references/../'):]
        if local in ids:
            return f'href="#{ids[local]}"'
        if not target.startswith(('https://','http://','mailto:')) and (ROOT/local).exists():
            kind = 'tree' if (ROOT/local).is_dir() else 'blob'
            return f'href="https://github.com/jason840709/let-chatgpt-say-like-person/{kind}/v{VERSION}/{local}"'
        return m[0]
    rendered = re.sub(r'href="([^"]+)"',fix_link,rendered)
    articles.append(f'<article id="{ids[name]}"><div class="filebar"><span>{html.escape(name)}</span><button type="button" data-copy="{ids[name]}">複製此檔原文</button></div>{rendered}</article>')
    nav.append(f'<a href="#{ids[name]}"><span>{i+1:02d}</span>{html.escape(label)}</a>')

data = json.dumps(texts,ensure_ascii=False).replace('<','\\u003c')
page='''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>講人話 Skill v2.8.1｜離線閱讀</title>
<style>
:root{color-scheme:light;--ink:#243328;--muted:#5e6a60;--line:#d9dfd5;--paper:#f7f7f0;--accent:#315b42}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:var(--paper);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"PingFang TC","Noto Sans TC",sans-serif;line-height:1.85}header{padding:44px 5vw 28px;border-bottom:1px solid var(--line);background:#eaf0e4}header .version{font-size:13px;letter-spacing:.1em;color:var(--accent)}header h1{font-size:clamp(28px,4vw,42px);letter-spacing:.03em;margin:4px 0 8px}header p{max-width:740px;margin:0;color:var(--muted)}.layout{display:grid;grid-template-columns:235px minmax(0,860px);gap:40px;max-width:1250px;margin:auto;padding:32px 28px}aside{align-self:start;position:sticky;top:24px}aside a{display:flex;gap:12px;padding:8px 10px;text-decoration:none;color:var(--ink);border-radius:5px}aside a:hover,aside a:focus-visible{background:#e4ecdf}aside span{color:var(--muted);font-size:12px;padding-top:3px}.download{display:inline-block;color:var(--accent);font-weight:600;margin-top:16px}main{min-width:0}article{background:#fffefa;border:1px solid var(--line);border-radius:8px;margin-bottom:32px;padding:28px 34px;overflow-wrap:anywhere}article h1{font-size:25px;line-height:1.5;margin-top:24px}article h2{font-size:21px;margin-top:32px}article h3{font-size:18px;margin-top:26px}article a{color:var(--accent);text-underline-offset:3px}p{margin:12px 0}li{margin:5px 0}.filebar{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-bottom:14px;border-bottom:1px solid var(--line);font:12px/1.5 ui-monospace,monospace;color:var(--muted)}button{font:inherit;font-family:inherit;border:1px solid var(--line);border-radius:5px;padding:7px 10px;background:#f1f4eb;color:var(--ink);cursor:pointer;white-space:nowrap}button:focus-visible{outline:2px solid var(--accent);outline-offset:3px}blockquote{border-left:3px solid #93ac87;margin:18px 0;padding:2px 18px;color:#415443;background:#f2f5ed}table{border-collapse:collapse;width:100%;font-size:14px;display:block;overflow-x:auto}td,th{border:1px solid var(--line);text-align:left;padding:9px 11px;vertical-align:top}th{background:#eef2e8}code{font-size:.9em;background:#edf0e8;padding:2px 4px;border-radius:3px}pre{overflow:auto;background:#edf0e8;padding:16px;font-size:13px}hr{border:0;border-top:1px solid var(--line);margin:28px 0}.hint{font-size:13px;color:var(--muted);margin:20px 10px}#status{position:fixed;bottom:20px;right:20px;max-width:calc(100vw - 40px);padding:10px 16px;border-radius:6px;background:#243328;color:white;box-shadow:0 4px 20px #0002}#status:empty{display:none}@media(max-width:760px){header{padding:28px 22px}.layout{display:block;padding:20px 14px}aside{position:static;display:grid;grid-template-columns:1fr 1fr;gap:2px;margin-bottom:20px;font-size:14px}.hint{grid-column:1/-1}article{padding:20px 18px}.filebar{font-size:11px}article h1{font-size:22px}article h2{font-size:19px}}@media print{aside,button,.download,#status{display:none}.layout{display:block;padding:0}article{border:0;padding:0;break-before:page}header{background:white}}
</style></head><body><header><div class="version">JASON · VERSION 2.8.1</div><h1>讓 ChatGPT 正常說人話</h1><p>把對象、理由、證據與必要條件說清楚。這份離線閱讀頁由同版原始檔產生，包含核心原則與全部細則。</p><a class="download" href="https://github.com/jason840709/let-chatgpt-say-like-person/releases/download/v2.8.1/let-chatgpt-say-like-person-v2.8.1.zip" download>下載完整 Skill ZIP</a></header><div class="layout"><aside>NAV<p class="hint">安裝請使用完整 ZIP。複製單一檔案不包含其他參考細則。頁內搜尋可用瀏覽器的尋找功能。</p></aside><main>ARTICLES</main></div><div id="status" role="status" aria-live="polite"></div><script type="application/json" id="sources">DATA</script><script>
const sources=JSON.parse(document.getElementById('sources').textContent);let timer;
async function copySource(id){const value=sources[id];let ok=false;try{await navigator.clipboard.writeText(value);ok=true}catch(e){const box=document.createElement('textarea');box.value=value;box.style.position='fixed';box.style.opacity='0';document.body.appendChild(box);box.select();ok=document.execCommand('copy');box.remove()}const status=document.getElementById('status');status.textContent=ok?'已複製此檔原文。安裝時請保留完整參考檔。':'無法自動複製，請開啟對應的 Markdown 原始檔。';clearTimeout(timer);timer=setTimeout(()=>{status.textContent=''},4500)}
document.querySelectorAll('[data-copy]').forEach(button=>button.addEventListener('click',()=>copySource(button.dataset.copy)));
</script></body></html>'''
page=page.replace('NAV',''.join(nav)).replace('ARTICLES',''.join(articles)).replace('DATA',data)
(ROOT/'index.html').write_text(page)
package_paths = [name for name, _ in NAMES] + ['agents/openai.yaml', 'assets/icon.svg']
package_paths += ['docs/v2.8.1-size-comparison.json', 'docs/validation-examples-v2.8.1.json', 'docs/package-validation-v2.8.1.json']
files = sorted(SKILL / name for name in package_paths)
assert all(f.is_file() for f in files)
manifest={str(f.relative_to(SKILL)): {'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files}
archive=DIST/f'{SKILL_NAME}-v{VERSION}.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for f in files:
        info=zipfile.ZipInfo(f'{SKILL_NAME}/{f.relative_to(SKILL).as_posix()}',date_time=(2026,10,18,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o644<<16
        z.writestr(info,f.read_bytes())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(files)
    for f in files: assert z.read(f'{SKILL_NAME}/{f.relative_to(SKILL).as_posix()}')==f.read_bytes()
(DIST/'package-manifest.json').write_text(json.dumps({'version':VERSION,'files':manifest,'zip_bytes':archive.stat().st_size,'zip_sha256':hashlib.sha256(archive.read_bytes()).hexdigest()},ensure_ascii=False,indent=2)+'\n')
print(f'Built {archive.name}: {len(files)} files, {archive.stat().st_size} bytes')
print(f'Offline reader: {len(NAMES)} source documents')

(DIST/'SHA256SUMS.txt').write_text(''.join(f'{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n' for f in [archive, ROOT/'index.html', DIST/'package-manifest.json']),encoding='utf-8')
