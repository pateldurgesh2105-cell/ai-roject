# Peblo AI Backend Engineer Challenge

This prototype AI-driven backend pipeline ingests educational PDFs, converts content into structured chunks, and generates adaptive quizzes using LLMs (Gemini).

## Features
- **Content Ingestion:** Extracts text from PDFs and stores it in chunks with metadata.
- **AI Quiz Generation:** Uses Gemini AI to generate MCQs, True/False, and Fill-in-the-blank questions.
- **Adaptive Difficulty:** Adjusts difficulty levels for subsequent questions based on student performance.
- **Traceability:** Maintains a link between generated questions and the source content chunk.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** SQLite with SQLAlchemy
- **AI:** Google Gemini (Generative AI)
- **PDF Processing:** PyMuPDF (fitz)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd peblo-challenge
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file from the example:
   ```bash
   cp .env.example .env
   ```
   Add your Gemini API Key in the `.env` file:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`.

## API Documentation
Interactive docs are available at `http://localhost:8000/docs`.

### Key Endpoints
- `POST /ingest`: Upload a PDF and process it. (Requires `grade`, `subject`, `topic`).
- `POST /generate-quiz/{doc_id}`: Generate quiz questions for a specific document.
- `GET /quiz`: Retrieve quiz questions (optional filters: `topic`, `difficulty`).
- `POST /submit-answer`: Submit an answer and get adaptive difficulty feedback.

**Note:** For the challenge, ensure you upload the provided PDFs (Grade 1 Math, Grade 3 Science, Grade 4 English) using the `/ingest` endpoint with their respective metadata.

## Implementation Details
- **Adaptive Logic:** The system increases difficulty by 1 level for correct answers and decreases it by 1 for incorrect ones (within levels 1-3).
- **Structured Output:** All generated questions are stored with a `chunk_id` for full traceability to the source material.
