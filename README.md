## 개발 환경 구성

> Python 3.12 이상이 필요합니다.

### Valkey 구성
```sh
docker run --rm -d -p 6379:6379/tcp valkey/valkey:latest
```

### Poetry 환경 구성

#### Linux & MacOS
```sh
python -m venv .venv
. .venv/bin/activate
```

#### Windows
```powershell
python -m venv .venv
. .venv/Scripts/activate
```

```sh
pip install poetry
```

### 종속성 설치

```sh
poetry install
```

### 인메모리 DB를 위한 aiosqlite 설치

```sh
pip install aiosqlite
```

### 서버 실행

```sh
python -m backend
```