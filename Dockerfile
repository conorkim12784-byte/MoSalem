FROM python:3.10-slim

WORKDIR /app

# Install ntpsec-ntpdate for time sync (ntpdate obsolete in Debian Trixie)
RUN apt-get update && apt-get install -y ntpsec-ntpdate && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ntpdate -u pool.ntp.org || true && python bot.py
