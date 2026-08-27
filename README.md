<div align="center">

# 🚀 CareerPulse AI

### Your Professional AI Career Advisor & Skill Gap Analyzer

**[🌐 Live Demo: career-pulse-ai.fastapicloud.dev](https://career-pulse-ai.fastapicloud.dev)**

---

## 1. Problem Statement
Job seekers often struggle to understand if their skills match a specific job role. They waste time applying to jobs they are unqualified for, or miss out on roles they could easily get with a little upskilling. Manually comparing a resume against hundreds of job descriptions is time-consuming and prone to human error.

## 2. Objective
To build an intelligent web application that automatically extracts skills from a user's CV (including education and experience context) and recommends the **Top 10 most suitable career paths** with a match percentage and a personalized list of "Skills to Learn" (The Gap).

## 3. Dataset
The system uses two primary JSON files:
- **`skills.json`**: A database of 300+ technical and soft skills (Python, Java, AI, Teaching, etc.).
- **`jobs.json`**: A structured database of 200+ job profiles across various domains (IT, Medical, Engineering, Business, Teaching, etc.), each containing a description, salary range, and required skills.

## 4. Data Preprocessing
- **Text Extraction:** CVs are parsed using `pdfplumber` for high-quality text extraction, with a fallback to `PyPDF2` and `python-docx` for Word files.
- **OCR Handling:** For scanned PDFs and images, `pytesseract` is used locally to extract text. (Cloud limitations noted below).
- **Normalization:** All text and skills are converted to lowercase to ensure case-insensitive matching.
- **Filtering:** Soft skills (Communication, Leadership) are excluded from the primary technical scoring to avoid false matches (e.g., a Doctor matching a Chef because of soft skills).

## 5. Exploratory Data Analysis (EDA)
- The job database is categorized into distinct sectors (Tech, Medical, Education, Finance, etc.).
- Analysis reveals that most jobs require a combination of 4-8 specific hard skills.
- The "Skills Database" provides a broad vocabulary mapping, allowing the system to detect skills even if they are mentioned in the summary or experience section of the CV.

## 6. Model Architecture
This is a **Rule-Based Expert System** (AI logic). It uses a weight-based scoring mechanism:
1. **Skill Match Score (70% weight):** Calculates the percentage of required job skills found in the user's CV.
2. **Education Context Score (30% weight):** A background detector checks for keywords (e.g., "Software Engineering", "MBBS") to add a bonus if the user's background perfectly aligns with the specific job domain.

## 7. Algorithms Tested
- **Simple Keyword Matching:** Initial version matched only exact keywords, leading to false positives.
- **SpaCy + SkillNer (AI NLP):** Implemented and tested locally, but removed due to strict library conflicts on the free cloud hosting environment.
- **Hybrid Scoring Algorithm (Final):** Finalized using Case-Insensitive Hard Skill Matching + Education Context Bonus to filter out irrelevant jobs and accurately rank candidates.

## 8. Evaluation Metrics
- **Match Percentage:** Calculated as `(Matched Hard Skills / Total Required Hard Skills) * 100`.
- **Gap Analysis:** Identifies the remaining required skills (Missing Skills) to guide the user's learning path.
- **Accuracy:** Manually tested against multiple CVs to ensure the top results are highly relevant to the user's specific field.

## 9. Results
- The system successfully identifies a user's technical profile. For example, a Software Engineering student gets:
  - **Software Engineer: 86% Match**
  - **Programming Instructor: 60% Match**
  - **AI/ML Engineer: 36% Match**
- Each result clearly displays the salary range and the exact skills the user needs to learn (e.g., "SQL, Docker") to reach a 100% match.

## 10. Limitations
- **Cloud OCR Limitation:** The current free FastAPI Cloud tier does not support system-level `Tesseract`/`Poppler` installations, limiting OCR support to the local environment.
- **Static Knowledge Base:** The system relies on the predefined `jobs.json` and `skills.json`. It cannot understand highly contextual or nuanced "Creative Skills" found in non-standard CVs.

## 12. Future Improvements
- **True AI Integration:** Integrate OpenAI or Gemini APIs for fully generative Gap Analysis and Summary generation.
- **Dynamic Database:** Implement a feature to scrape live job descriptions from LinkedIn or Indeed.
- **Cloud OCR:** Upgrade hosting to support Docker environments for full scanned PDF and Image support.

## 13. Installation
1. Clone the repository:
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
🔗 Portfolio: https://maryamghaffar1234m-png.github.io/Maryam_Portfolio/
    LinkedIn: maryam-ghaffar-62551837b   
    Made with ❤️ by Maryam Ghaffar – Software Engineering student at LCWU

© 2026 Maryam Ghaffar | Crafting digital experiences, one line at a time
