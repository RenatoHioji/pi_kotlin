FROM python:3.12.7-alpine3.20

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

ENTRYPOINT ["sh", "-c", "echo 'Waiting for database...'; while ! nc -z db 5432; do sleep 2; done; echo 'Connected to database.'; gunicorn -w 1 -b 0.0.0.0:4000 app:app"]
