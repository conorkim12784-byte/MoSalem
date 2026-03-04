FROM python:3.10-slim

WORKDIR /app

# Install ntpdate for time sync
RUN apt-get update && apt-get install -y ntpdate && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ntpdate -u pool.ntp.org || true && python bot.py
