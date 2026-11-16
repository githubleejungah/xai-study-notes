"""claude.ai 아티팩트용 본문(src/*.html)에 문서 머리(doctype · charset · noindex)를 붙여 GitHub Pages 페이지로 만든다.
사용: python tools/build.py   (저장소 루트에서)
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
HEAD = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="robots" content="noindex,nofollow">'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n')
PAGES = {'src/notes.html': 'notes/index.html', 'src/quiz.html': 'quiz/index.html'}
for src, out in PAGES.items():
    body = (ROOT / src).read_text(encoding='utf-8')
    (ROOT / out).write_text(HEAD + body + '\n</body></html>\n', encoding='utf-8')
    print('built', out)
