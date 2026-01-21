FROM python:3.11-slim

WORKDIR /app

# Install only what's needed (no gcc — pure Python)
RUN pip install --no-cache-dir flask gunicorn

# Create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

COPY app.py .

# Switch to non-root
USER appuser

EXPOSE 5000

# Use multiple workers (CPU-bound inference)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
