# AI Resume Analyzer

A FastAPI-based backend system that analyzes a candidate's resume against a job description using Large Language Model (LLM) integration.

## 🚀 Features

- REST API built with FastAPI
- LLM integration (Gemini API)
- Structured JSON response
- Prompt engineering for resume-job matching
- Input validation using Pydantic
- Error handling & fallback mechanism
- Modular service architecture

## 🛠 Tech Stack

- Python
- FastAPI
- Gemini API (Google Generative AI)
- Pydantic
- dotenv

## 📂 Project Structure

```
ai-resume-analyzer/
├── app/
│   ├── main.py
│   ├── models/
│   │   └── schemas.py
│   └── services/
│       └── gpt_service.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```
