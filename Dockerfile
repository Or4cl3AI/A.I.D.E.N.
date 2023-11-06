FROM python:3.8-slim-buster

WORKDIR /app

COPY aiden /app/aiden
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "-c", "import aiden; aiden_instance = aiden.Aiden()"]
