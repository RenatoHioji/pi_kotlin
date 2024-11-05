FROM python:3.12.7-alpine3.20

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4000

CMD CD app & py ./app.py
