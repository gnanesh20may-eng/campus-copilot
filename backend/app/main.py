from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.upload import router as upload_router
from seed_sample_data import seed_sample_data

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

app = FastAPI(title="Campus Copilot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://PLACEHOLDER-VERCEL-URL.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_seed_data():
    seed_sample_data()


app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Campus Copilot backend is running"}
