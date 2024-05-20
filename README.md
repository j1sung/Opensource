# Study OpensourceSW
### DKU 소프트웨어학과 32202546 안지성
### 1. Django 과제 -> TDL(To-do List App) 구현
  - **테스트:** ```python manage.py runserver``` -> localhost:8000 접속

### 2. Docker 과제 -> Django To-do List App을 Docker 컨테이너로 구현
**1) 단일 컨테이너로 구현**
```
TDL1/
│
├── myapp/
│   ├── __pycache__/
│   ├── migrations/
│   └── templates/
│       └── myapp/
│           ├── base.html
│           ├── index.html
│           └── update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── TDL/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── db.sqlite3
├── Dockerfile
├── manage.py
└── requirements.txt
```
- dockerfile 생성(requirements.txt 사용), DB(sqllite3 사용)
- **테스트:**
  - docker image build: ```docker build -t tdl .```
  - docker container run: ```docker run -p 8000:8000 tdl``` -> localhost:8000 접속

**2) 멀티 컨테이너로 구현**
```
TDL2/
│
├── myapp/
│   ├── __pycache__/
│   ├── migrations/
│   └── templates/
│       └── myapp/
│           ├── base.html
│           ├── index.html
│           └── update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── TDL/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```
- dockerfile 작성, docker-compose.yml 작성, settings.py 설정(DB 정보 mysql로 수정)
- **테스트:**
  - ```docker-compose up --build``` -> if 포트충돌 발생 -> ```netstat -ano | findstr :해당포트```로 사용중인 프로세스 PID 찾기
  -> 작업관리자(ctrl+shift+esc), 세부정보 메뉴에서 해당 PID 프로세스 작업 종료 후 다시 ```docker-compose up --build``` 실행
  - 포트충돌 오류가 없다면 localhost:3000 접속 시도 -> if 경로 error 발생시 ctrl+c로 종류 후 ```docker-compose up -d --build```로 백그라운드 실행
  -> ```docker-compose exec web python3 manage.py migrate```로 migrate 해줌 -> 다시 localhost:3000 접속시 접속됨!
    (if 3000포트가 안되면 docker-compose.yml 파일에서 web service ports:에서 3000:8000 -> 8000:8000 변경 후 다시 진행)
