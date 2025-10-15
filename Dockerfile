FROM python:3.11-alpine

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python", "app.py"]
