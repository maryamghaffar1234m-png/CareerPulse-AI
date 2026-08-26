FROM python:3.11

# Cloud ke liye Tesseract aur Poppler install karna zaroori hai (Images/OCR support)
RUN apt-get update && apt-get install -y tesseract-ocr poppler-utils

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Hugging Face ka default port 7860 hota hai, isliye yeh port use karein
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]