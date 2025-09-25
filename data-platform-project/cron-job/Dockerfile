FROM ubuntu:20.04

# Install Python and system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.9 \
        python3-pip \
        python3.9-dev \
        libnss3 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdrm2 \
        libxkbcommon0 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxrandr2 \
        libgbm1 \
        libasound2 \
        libxshmfence1 \
        wget curl cron && \
    rm -rf /var/lib/apt/lists/*

# Ensure python and pip commands point to Python 3.9
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (Chromium only)
RUN pip install --no-cache-dir playwright && \
    playwright install chromium

# Copy application files
COPY . .

# Add cron job
RUN echo "* * * * * python /app/script.py >> /var/log/cron.log 2>&1" > /etc/cron.d/cron-job \
    && chmod 0644 /etc/cron.d/cron-job \
    && crontab /etc/cron.d/cron-job

# Run cron in foreground
CMD ["cron", "-f"]
