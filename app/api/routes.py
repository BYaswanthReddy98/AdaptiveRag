
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from app.services.pdf_parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.document import Document

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
    text = clean_text(text)
    document = Document(
    filename=file.filename,
    content=text,
    content_type=file.content_type
)

    return {
    "filename": document.filename,
    "content_type": document.content_type,
    "text_length": len(document.content),
    "metadata": document.metadata
}
  