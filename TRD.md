# Technical Requirements Document (TRD) - AI Resume Suite 📄🚀

## 1. Project Overview
The **AI Resume Suite** is a comprehensive tool designed to bridge the gap between job seekers and recruitment requirements. By leveraging Large Language Models (LLMs), specifically GPT-4o-mini via OpenRouter, the system provides deep semantic analysis of resumes against specific job descriptions, offers optimization suggestions, and generates tailored, ATS-friendly resumes.

## 2. Objectives
- **Automate Resume Squaring:** Reduce the time candidates spend manually tailoring resumes.
- **Identify Skill Gaps:** Provide actionable insights into what a candidate needs to learn or highlight.
- **High-Quality Output:** Provide professional PDF generation to ensure the final product is ready for submission.
- **User-Friendly Interface:** Offer a seamless, modern web experience for both text-based and PDF-based inputs.

## 3. Product Features
### 3.1 Resume Analysis
- **Match Score:** A percentage-based ranking of resume relevance to a Job Description (JD).
- **Strengths & Weaknesses:** Detailed lists of where the candidate aligns and where they fall short.
- **Improvement Suggestions:** Strategic advice on how to rephrase or add missing information.

### 3.2 PDF Processing
- **Extraction:** Automated text extraction from uploaded `.pdf` files using `pdfplumber`.
- **Downloadable Results:** Generation of a new, optimized PDF resume based on AI tailoring.

### 3.3 AI Resume Tailoring
- **Semantic Rewriting:** The system doesn't just swap keywords; it rephrases experiences to highlight relevant impact.
- **Tone Adjustment:** Uses professional action verbs and achievement-oriented language.

## 4. Technical Architecture
The project follows a decoupled architecture with a clear separation between frontend and backend.

### 4.1 Frontend
- **Technology:** Vanilla JavaScript (ES6+), HTML5, CSS3.
- **Design:** Modern Dark Theme using custom CSS variables, flexbox, and glassmorphism-inspired components.
- **State Management:** Local JavaScript state for handling tab switching (Text vs. PDF) and API results.

### 4.2 Backend
- **Framework:** FastAPI (Python 3.9+).
- **AI Integration:** OpenAI SDK connected to **OpenRouter API** (Model: `openai/gpt-4o-mini`).
- **PDF Handling:** 
  - **Parsing:** `pdfplumber` for extraction.
  - **Generation:** `fpdf2` for building premium PDF documents.
- **Environment:** `python-dotenv` for secure secret management.

## 5. System Design & Data Flow
### 5.1 Directory Structure
- `/frontend`: Static assets (`index.html` with embedded styles/logic).
- `/backend`: Core application logic.
  - `app/main.py`: Endpoint routing and server configuration.
  - `app/models`: Pydantic schemas for data validation.
  - `app/services`: Modular logic for AI, PDF parsing, and PDF generation.

### 5.2 API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the frontend application. |
| `POST` | `/analyze` | Analyzes JSON-based resume and JD text. |
| `POST` | `/analyze-pdf` | Analyzes a PDF file upload against a JD. |
| `POST` | `/tailor` | Generates a tailored resume from text. |
| `POST` | `/tailor-pdf` | Generates a tailored resume from a PDF file. |
| `POST` | `/download-pdf` | Converts tailored text into a downloadable PDF. |

## 6. Functional Requirements
- **FR1:** The system must accept at least 50 characters for both resume and JD to ensure quality analysis.
- **FR2:** PDF extraction must support multi-page documents.
- **FR3:** AI prompts must ensure that no false information is fabricated during the "tailoring" process.
- **FR4:** The system must use a fallback mechanism ("Mock Response") if the AI provider is unreachable.

## 7. Non-Functional Requirements
- **Performance:** Analysis should complete within 3-5 seconds using GPT-4o-mini.
- **Security:** API keys must never be hardcoded and must be loaded via `.env`.
- **Scalability:** The backend should be stateless to allow for horizontal scaling in cloud environments.
- **Usability:** The UI must be responsive and provide clear loading indicators during AI processing.

## 8. Development Roadmap
- [x] Phase 1: Core Analysis Engine (Gemini/GP4).
- [x] Phase 2: PDF Parsing & Upload Support.
- [x] Phase 3: Premium UI Design.
- [x] Phase 4: Resume Tailoring & PDF Generation.
- [x] Phase 5: Project Restructuring (Frontend/Backend).
- [ ] Phase 6: Cloud Deployment (AWS/Vercel/Render).
- [ ] Phase 7: Multi-Language Support.

---
**Version:** 2.1.0  
**Last Updated:** February 26, 2026
