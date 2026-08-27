<div align="center">

# 🚀 CareerPulse AI

### Your Professional AI Career Advisor & Skill Gap Analyzer

**[🌐 Live Demo: career-pulse-ai.fastapicloud.dev](https://career-pulse-ai.fastapicloud.dev)**

![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Platform](https://img.shields.io/badge/Platform-FastAPI%20%7C%20Python-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 💡 About The Project

CareerPulse AI is an intelligent web application designed to bridge the gap between job seekers and the job market. It goes beyond simple keyword matching by analyzing your CV's **education background, experience, and technical skills** to predict your best career paths.

It calculates your eligibility score for each job, shows you **what skills you already have**, and creates a personalized roadmap of **what you need to learn next** to get hired.

## ✨ Key Features

- **🧠 Smart Skill Extraction:** Automatically identifies 300+ technical and soft skills from your CV.
- **🎯 Personalized Career Matching:** Compares your profile against a database of **200+ Job Profiles** (IT, Medical, Business, Engineering, Teaching, etc.).
- **📊 Visual Match Score:** Displays an intuitive progress bar showing your exact match percentage for each job role.
- **📈 Gap Analysis:** Clearly lists the "Future Skills to Learn" (The Gap) tailored for each career.
- **📄 Multi-Format Support:** Accepts Text-based PDFs, Word (DOCX), and local Image (JPG/PNG) files.
- **🎨 Modern UI:** Sleek, dark-themed, and fully responsive user interface.

## ⚙️ How It Works

1. **User Uploads CV:** The system securely extracts raw text from the uploaded file.
2. **Education Analysis:** Detects the user's educational background (e.g., Software Engineering, Medical).
3. **Skill Extraction:** Cross-references the text with a comprehensive skills database.
4. **Smart Matching:** Computes an eligibility score based on a 70% Skill match and 30% Education background match.
5. **Roadmap Generation:** Returns the Top 10 matching careers with their salary ranges and specific missing skills.

> **⚠️ Note:** The live cloud version supports Text-Based PDFs and DOCX files. (Scanned PDFs and Images require advanced OCR tools like Tesseract, which are currently enabled in the local environment).

## 🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core Backend Language |
| **FastAPI** | High-performance Web Framework & API |
| **PyPDF2 / pdfplumber / python-docx** | CV Text Extraction |
| **Pytesseract** | OCR for Images / Scanned PDFs (Local Setup) |
| **HTML / CSS / JavaScript** | Modern Frontend Interface |

## 🚀 Deployment

This project is currently live and hosted on **FastAPI Cloud** (Free Tier). 
**Live URL:** [https://career-pulse-ai.fastapicloud.dev](https://career-pulse-ai.fastapicloud.dev)

## 💻 Local Development

To run this project on your own machine, follow these steps:

**Prerequisites:** Python 3.11+, Tesseract OCR (for images)

1. Clone the repository
   ```bash
   git clone https://github.com/maryamghaffar1234m-png/CareerPulse-AI.git
   cd CareerPulse-AI/backend
2. Install dependencies
                 pip install -r requirements.txt
3.  Run the server
                python -m uvicorn main:app --reload
4. Open your browser and visit:
                http://127.0.0.1:8000
   📄 License
Distributed under the MIT License.

👩‍💻 Author: Maryam Ghaffar
📧 Email: maryamghaffar1234m@gmail.com
🔗 Portfolio: 
    LinkedIn: 
