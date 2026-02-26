# AI Resume Analyzer 📄🚀

An LLM-powered Resume vs Job Description Matching System built with **FastAPI** and **Google Gemini 2.0 Flash**.

## 🌟 Features

- **Match Percentage:** Instant calculation of how well a resume fits a job description.
- **Skill Gap Analysis:** Identification of missing skills required for the role.
- **Strengths Identification:** Highlights the key areas where the candidate excels.
- **Improvement Suggestions:** Actionable feedback to improve the resume for a specific role.
- **JSON API:** Structured responses ready for frontend integration.
- **Robust Error Handling:** Fallback mechanisms to ensure API availability.

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **AI Model:** Google Gemini 2.0 Flash
- **Validation:** Pydantic
- **Testing:** Pytest & HTTPX (TestClient)

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Google Gemini API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mentachaitanya/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup:**
   Create a `.env` file in the root directory and add your API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## 🖥️ Usage

### Start the Server
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### API Documentation
Interactive docs: `http://127.0.0.1:8000/docs`

### Example Request
**Endpoint:** `POST /analyze`

```json
{
  "resume_text": "Experienced Python developer with strong background in FastAPI and Cloud deployments...",
  "job_description": "We are looking for a backend engineer proficient in Python, FastAPI, and AWS..."
}
```

### Example Response
```json
{
  "match_percentage": 85.0,
  "missing_skills": ["AWS Lambda", "Docker"],
  "strengths": ["Python", "FastAPI"],
  "improvement_suggestions": ["Include specific AWS projects in the experience section."],
  "note": null
}
```

## 🧪 Testing

Run unit tests using Pytest:
```bash
python -m pytest -v
```

## 📂 Project Structure

```
ai-resume-analyzer/
├── app/
│   ├── main.py            # Entry point & API routes
│   ├── models/
│   │   └── schemas.py     # Pydantic data models
│   └── services/
│       └── gpt_service.py # Gemini AI integration logic
├── tests/
│   └── test_main.py       # API endpoint tests
├── .env                   # Environment variables (Secrets)
├── .gitignore             # Files to ignore in Git
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---
*Developed with ❤️ by mentachaitanya*
