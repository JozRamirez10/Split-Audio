FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# ==========================================
# Install system audio dependencies
# ==========================================
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

ARG PYTORCH_INSTALL_ARGS=""

# ==========================================
# Install environment audio dependencies
# ==========================================
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch torchvision torchaudio ${PYTORCH_INSTALL_ARGS} && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7004"]