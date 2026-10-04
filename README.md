# 🎯 랜덤 룰렛 (Cafe Roulette)

Vue 3, Tailwind CSS, HTML5 Canvas 기반의 N개 입력 지원 웹 룰렛 애플리케이션입니다.

## 🚀 빠른 시작 (uv 활용)

이 프로젝트는 `uv`를 이용하여 파이썬 가상 환경을 관리하고 웹 서버를 실행합니다.

### 1. 가상환경 생성 & 서버 실행
```bash
# start.sh 실행 (가상환경 자동 확인 및 웹 서버 시작)
./start.sh
```

또는 `uv` 명령어를 직접 사용:
```bash
# uv 가상환경 생성
uv venv

# 파이썬 HTTP 서빙 스크립트 실행
uv run python serve.py

# 또는 기본 http.server 모듈 직접 실행 (8000 포트)
uv run python -m http.server 8000
```

### 2. 브라우저 접속
서버 실행 후 자동으로 기본 브라우저가 열리며, [http://localhost:8000](http://localhost:8000) 주소로 접속하실 수 있습니다.

## 📁 프로젝트 구조
- `index.html`: 룰렛 웹 앱 (Vue 3, Tailwind CSS, HTML5 Canvas)
- `serve.py`: HTTP 서빙 파이썬 스크립트 (포트 자동 재할당 및 브라우저 자동 오픈 지원)
- `start.sh`: uv 기반 원클릭 서버 실행 쉘 스크립트
- `pyproject.toml`: uv 프로젝트 구성 파일
- `.venv/`: uv 파이썬 가상환경 디렉토리
