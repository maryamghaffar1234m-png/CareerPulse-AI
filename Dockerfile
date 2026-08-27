FROM python:3.11

# Cloud server par Tesseract aur Poppler install karna zaroori hai (Images/Scanned PDF support)
RUN apt-get update && apt-get install -y tesseract-ocr poppler-utils

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Port ko 7860 par rakhein (FastAPI Cloud ka default)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
