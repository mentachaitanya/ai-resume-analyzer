# AI Resume Suite 📄🚀

A comprehensive, LLM-powered toolkit to analyze, optimize, and tailor resumes against job descriptions. Built with **FastAPI** and **OpenRouter (GPT-4o-mini)**.

## 🌟 Features

- **Match Analysis:** Instant calculation of how well a resume fits a specific job description.
- **Skill Gap Identification:** Detects missing technical and soft skills required for the role.
- **PDF Support:** Directly upload `.pdf` resumes for analysis—no manual copy-pasting required.
- **AI Resume Tailoring:** Automatically rewrites and optimizes your resume to align perfectly with a target JD.
- **Professional PDF Export:** Download your AI-tailored resume as a clean, professionally formatted PDF.
- **Rich Dashboard:** A premium, dark-mode web interface for a seamless user experience.

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Vanilla JS, HTML5, CSS3 (Modern Dark Theme)
- **AI Engine:** GPT-4o-mini (via OpenRouter)
- **PDF Layout:** fpdf2
- **PDF Parsing:** pdfplumber
- **Validation:** Pydantic

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- [OpenRouter API Key](https://openrouter.ai/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mentachaitanya/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Navigate to the Backend:**
   ```bash
   cd backend
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Environment Setup:**
   Create a `.env` file inside the `backend/` directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_key_here
   ```

## 🖥️ Usage

### Start the Application
From the `backend/` directory:
```bash
uvicorn app.main:app --reload
```
The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### API Documentation
Interactive Swagger docs: `http://127.0.0.1:8000/docs`

## 📂 Project Structure

```
ai-resume-analyzer/
├── frontend/
│   └── index.html         # Premium Web Dashboard
├── backend/
│   ├── app/
│   │   ├── main.py        # FastAPI Entry Point
│   │   ├── models/        # Pydantic Schemas
│   │   └── services/      # AI, PDF, & Parser Logic
│   ├── tests/             # Pytest Suite
│   ├── .env               # API Configuration
│   └── requirements.txt   # Backend Dependencies
└── README.md              # Project Documentation
```

---
*Developed with ❤️ by mentachaitanya*
