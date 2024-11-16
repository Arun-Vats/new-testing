FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]

# Expose the port for Telethon to listen on
EXPOSE 443

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:443/ || exit 1
