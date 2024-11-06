FROM python:3.12.7-alpine3.20

WORKDIR /app

COPY ./script.sh /scripts/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

ENTRYPOINT ["/scripts/script.sh"]
