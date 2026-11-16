# CLAUDE.md — xai-study-notes

## 무엇
매치업 X+AI 심화과정 개인 학습 자료(정적 HTML)를 GitHub Pages로 공개하는 저장소.

## 규칙
- 정본은 `src/*.html`이다. `notes/index.html` · `quiz/index.html`은 `tools/build.py`가 만드는 생성물이므로 직접 고치지 않는다.
- 모든 페이지에 `noindex`를 유지한다. `robots.txt`는 전체 차단을 유지한다.
- 강의 슬라이드 · 녹취 문장을 길게 그대로 옮기지 않는다. 내 말로 줄여 쓰고 출처(교재 쪽수, 강의 시각)를 적는다.
- 강사는 항상 "강사님"으로 부른다. 강사님 설명과 교재 · 공식 문서가 다르면 단정하지 말고 "교재 기준 답"과 함께 중립적으로 적는다.
- 비밀 값 · 개인정보를 넣지 않는다.
- 응답과 문서는 한국어, 짧은 문장. 용어는 처음 나올 때 풀어 쓴다.

## 자주 쓰는 명령
```bash
python tools/build.py          # 생성물 다시 만들기
python -m http.server 8765     # 로컬 미리보기
```
