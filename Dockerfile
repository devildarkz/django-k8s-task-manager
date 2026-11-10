# Stage 1: Build dependencies
FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

# Create and switch to a non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers", "3", "taskproject.wsgi:application"]