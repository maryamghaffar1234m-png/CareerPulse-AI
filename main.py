import pdfplumber
import os
import shutil
import json
import pytesseract
from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import FileResponse, PlainTextResponse, Response
from PyPDF2 import PdfReader
from PIL import Image
from pdf2image import convert_from_path
from docx import Document

# Tesseract ka path (Smart Code: Local aur Cloud dono ke liye)
if os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Apna live URL yahan paste karein (Isko change karna zaroori hai!)
_BASE_URL = "https://career-pulse-ai.fastapicloud.dev"

# HEAD Request Fix (Google ke liye)
@app.middleware("http")
async def handle_head_requests(request: Request, call_next):
    if request.method == "HEAD":
        request.scope["method"] = "GET"
        response = await call_next(request)
        response.body = b""
        return response
    return await call_next(request)

# SEO: robots.txt aur sitemap.xml
@app.get("/robots.txt", response_class=PlainTextResponse, include_in_schema=False)
async def robots_txt():
    return "User-agent: *\nAllow: /\n" + f"Sitemap: {_BASE_URL}/sitemap.xml\n"

@app.get("/sitemap.xml", include_in_schema=False)
async def sitemap_xml():
    content = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{_BASE_URL}</loc></url></urlset>'
    return Response(content=content, media_type="application/xml")

def load_json_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

SKILLS_DB = load_json_data("skills.json")
JOB_DATABASE = load_json_data("jobs.json")

SOFT_SKILLS = ["communication", "leadership", "teamwork", "time management", "problem-solving", "excel", "microsoft office"]

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    
    # 1. Sabse pehle pdfplumber try karo (best quality)
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except:
        pass

    # 2. Agar khali hai, toh PyPDF2 try karo
    if not text.strip():
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                text += page.extract_text() or ""
        except:
            pass

       # 3. Agar ab bhi khali hai (Scanned PDF), toh check karo OCR available hai ya nahi
    if not text.strip():
        # Check karo ke system par Poppler/Tesseract installed hai ya nahi (Local laptop)
        if os.path.exists(r'D:\poppler\Library\bin'):
            try:
                images = convert_from_path(file_path, poppler_path=r'D:\poppler\Library\bin')
                for img in images:
                    text += pytesseract.image_to_string(img) + " "
            except Exception as e:
                print(f"OCR Error: {e}")
        else:
            # Cloud par tools install nahi hain, isliye user ko friendly message do
            return "⚠️ Scanned PDF detected. Please upload a text-based PDF or DOCX file for analysis."

    return text

def extract_text_from_docx(file_path: str) -> str:
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read DOCX: {str(e)}")

def extract_text_from_image(file_path: str) -> str:
    try:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read Image: {str(e)}")

def extract_skills(text: str):
    text_lower = text.lower()
    found_skills = []
    for skill in SKILLS_DB:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return list(set(found_skills))

def extract_summary(text: str):
    return text[:150].replace('\n', ' ').strip() + "..." if text else "No text could be extracted."

def extract_experience(text: str):
    text_lower = text.lower()
    if "year" in text_lower or "internship" in text_lower or "experience" in text_lower:
        return "Professional experience or internships detected in CV."
    return "Entry-level candidate (No formal experience detected yet)."

@app.get("/")
def serve_frontend():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"message": "index.html not found"}

@app.post("/upload-cv/")
async def upload_cv(file: UploadFile = File(...)):
    file_path = None
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        ext = file.filename.lower().split('.')[-1]
        if ext == 'pdf':
            text = extract_text_from_pdf(file_path)
        elif ext == 'docx':
            text = extract_text_from_docx(file_path)
        elif ext in ['jpg', 'jpeg', 'png']:
            text = extract_text_from_image(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type! Please upload PDF, DOCX, JPG, or PNG.")
        
        user_skills = extract_skills(text)
        summary = extract_summary(text)
        experience = extract_experience(text)
        
        if os.path.exists(file_path):
            os.remove(file_path)

        text_lower_for_context = text.lower()
        education_background = []
        if "software engineering" in text_lower_for_context or "computer science" in text_lower_for_context or "bachelor" in text_lower_for_context or "it" in text_lower_for_context:
            education_background.extend(["Software Engineer", "AI / Machine Learning Engineer", "Data Scientist", "Full Stack Web Developer"])
        if "medical" in text_lower_for_context or "mbbs" in text_lower_for_context or "nursing" in text_lower_for_context:
            education_background.extend(["General Physician", "Registered Nurse", "Pharmacist"])
        if "teacher" in text_lower_for_context or "b.ed" in text_lower_for_context or "school" in text_lower_for_context:
            education_background.extend(["Primary School Teacher", "University Professor"])

        user_hard_skills = [s for s in user_skills if s.lower() not in SOFT_SKILLS]
        user_hard_skills_lower = [s.lower() for s in user_hard_skills]

        job_matches = []
        for job in JOB_DATABASE:
            required_skills = [s for s in job["required_skills"] if s.lower() not in SOFT_SKILLS]
            required_skills_lower = [s.lower() for s in required_skills]
            
            matched_skills = [s for s in required_skills if s.lower() in user_hard_skills_lower]
            missing_skills = [s for s in required_skills if s.lower() not in user_hard_skills_lower]
            
            if len(required_skills) > 0:
                percentage = int((len(matched_skills) / len(required_skills)) * 100)
            else:
                percentage = 0
            
            if job["title"] in education_background and len(matched_skills) > 0:
                percentage = min(percentage + 20, 100)
            
            if percentage <= 0:
                continue
            
            job_matches.append({
                "title": job["title"],
                "description": job["description"],
                "salary_range": job["salary_range"],
                "matched_percentage": percentage,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills
            })
        
        job_matches.sort(key=lambda x: x["matched_percentage"], reverse=True)
        filtered_jobs = job_matches[:10]

        return {
            "status": "success",
            "filename": file.filename,
            "summary": summary,
            "experience": experience,
            "user_skills": user_skills,
            "job_matches": filtered_jobs,
            "total_jobs_analyzed": len(JOB_DATABASE)
        }
        
    except Exception as e:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
