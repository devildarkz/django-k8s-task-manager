# Stage 1: Build dependencies
FROM python:3.12-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime image
FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
COPY . /app

# Create a non-root user for security
RUN useradd -m -u 1000 appuser && mkdir -p /home/appuser && chown -R appuser:appuser /app /home/appuser
USER appuser
ENV HOME=/home/appuser

EXPOSE 3000

CMD ["gunicorn", "taskproject.wsgi:application", "--bind", "0.0.0.0:3000", "--workers", "3"]