#!/bin/sh

echo "Running preliminary setup tasks..."
echo "Waiting for database..."
while ! nc -z "db" "5432"; do
  sleep 2
done
echo "Connected to database."

echo "Starting the application..."

gunicorn -w 4 -b 0.0.0.0:4000 app:app
