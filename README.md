# Campus Copilot

A full-stack Retrieval-Augmented Generation (RAG) chatbot for college documents.

## Project structure

```
backend/
├── app/
│   ├── main.py
│   ├── routes/chat.py
│   ├── routes/upload.py
│   ├── services/ingestion.py
│   ├── services/embeddings.py
│   ├── services/retriever.py
│   ├── services/llm.py
│   ├── db/vector_store.py
│   └── models/schemas.py
├── requirements.txt
├── .env.example
└── Dockerfile
frontend/
├── src/
│   ├── App.jsx
│   ├── api.js
│   ├── pages/Upload.jsx
│   ├── pages/Chat.jsx
│   ├── components/ChatWindow.jsx
│   ├── components/MessageBubble.jsx
│   └── components/SourceCitation.jsx
└── package.json
data/sample_docs/
docker-compose.yml
README.md
```

## Backend setup

1. Create a Python virtual environment inside the backend folder:
   - `cd backend`
   - `py -3.11 -m venv .venv`
   - `.\.venv\Scripts\activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your Anthropic key:
   - `copy .env.example .env`
4. Run the backend:
   - `uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`

## Frontend setup

1. `cd frontend`
2. `npm install`
3. `npm run dev`
4. Open the Vite URL (usually `http://127.0.0.1:5173`)

## How to use

1. Upload a PDF on the Upload page.
2. Switch to Chat and ask questions about the uploaded documents.
3. The chatbot returns a sourced answer and a list of citations.

## Notes

- Frontend defaults to backend URL `http://127.0.0.1:8000`.
- Set `VITE_API_URL` in `frontend/.env` to use another backend host.
- Sample PDFs may be placed in `data/sample_docs/` for ingestion tests.
