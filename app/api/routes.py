
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from app.services.pdf_parser import extract_text_from_pdf

router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":

        return {
        "error": "Only PDF files are allowed"
    }
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_to": file_path,
        "text_length": len(text)
    }
  