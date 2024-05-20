# 베이스 이미지로 Python 3.10 사용
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 의존성 설치 (선택 사항)
RUN apt-get update && apt-get install -y \
    build-essential \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . /app

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# 장고 애플리케이션의 포트를 외부로 노출
EXPOSE 8000

# 서버 시작 명령어
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]