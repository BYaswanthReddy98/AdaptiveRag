from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/ask")
def ask_question(data: Question):
    return {"received_question": data.question}