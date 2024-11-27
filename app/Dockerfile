# First stage: use Alpine to install FFmpeg
FROM alpine:3.20 AS ffmpeg_builder

RUN apk update && \
    apk add --no-cache ffmpeg

FROM python:3.12.7-alpine3.20

COPY --from=ffmpeg_builder /usr/bin/ffmpeg /usr/bin/ffmpeg
COPY --from=ffmpeg_builder /usr/lib/ /usr/lib/
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 4000

ENTRYPOINT ["sh", "-c", "echo 'Waiting for database...'; while ! nc -z db 5432; do sleep 2; done; echo 'Connected to database.'; gunicorn -w 1 -b 0.0.0.0:4000 app:app"]
