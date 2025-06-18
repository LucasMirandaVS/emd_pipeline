FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install pytest

COPY . .

# Rodar agent por padrão
CMD ["prefect", "agent", "start", "-q", "default"]
