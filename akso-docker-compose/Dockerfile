FROM python:3.9-slim

WORKDIR /app

COPY ./flask-web /app/flask-web

WORKDIR /app/flask-web

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]