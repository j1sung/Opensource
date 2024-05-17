# Study OpensourceSW
### DKU 소프트웨어학과 32202546 안지성
- Django 과제 -> TDL(To-do List App) 구현
  - 테스트: ```python manage.py runserver``` -> localhost:8000 접속
- Docker 과제 -> Django To-do List App를 Docker 컨테이너로 구현
  - dockerfile 생성(requirements.txt 사용)
  - docker image build: ```docker build -t tdl .```
  - docker container run: ```docker run -p 8000:8000 tdl```
