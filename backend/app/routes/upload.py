from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.models.schemas import UploadResponse
from app.services.ingestion import ingest_pdf

router = APIRouter(prefix="/upload", tags=["upload"])

UPLOAD_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_path = UPLOAD_DIR / file.filename
    content = await file.read()

    file_path.write_bytes(content)
    chunk_count = ingest_pdf(file_path, file.filename)
    if chunk_count == 0:
        raise HTTPException(status_code=400, detail="Uploaded PDF contained no extractable text.")

    return {"filename": file.filename, "chunks_added": chunk_count}
