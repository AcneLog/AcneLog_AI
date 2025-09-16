FROM --platform=$TARGETPLATFORM python:3.12-slim-bookworm

WORKDIR /app

# Debian Bookworm에서 OpenCV 의존성 설치
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY tflite_api_server.py .
COPY model.tflite .

EXPOSE 8000
CMD ["uvicorn", "tflite_api_server:app", "--host", "0.0.0.0", "--port", "8000"]