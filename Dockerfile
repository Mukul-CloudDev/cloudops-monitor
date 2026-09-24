FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir psutil

COPY scripts/health_check.py .

CMD ["python", "health_check.py"]
