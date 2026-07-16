# Campus Copilot — Frontend (Vite + React)

This is a minimal React frontend to work with the Campus Copilot backend.

Assumptions:
- Backend is available at http://127.0.0.1:8000 by default (FastAPI app).
- CORS is already enabled on the backend (the provided backend allows all origins).

Run locally:
1. cd into this folder
2. npm install
3. npm run dev
4. Open the URL shown by Vite (usually http://127.0.0.1:5173)

Configuration:
- To point the frontend at a different backend URL, set VITE_API_URL in a .env file (e.g. VITE_API_URL=https://your-host).

Notes:
- Upload uses the field name `file` and posts to POST /upload as FormData.
- Chat posts JSON { query } to POST /chat and expects a response like { answer: string, sources: [string] }.
