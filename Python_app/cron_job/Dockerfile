FROM python:3.11-slim

WORKDIR /app

# Installera cron innan pip/cron-körning
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && playwright install chromium

COPY . .

CMD ["sh", "-c", "echo '* * * * * python /app/cron_app.py' | crontab - && cron -f"]
