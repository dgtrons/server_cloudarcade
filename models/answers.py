from pydantic import BaseModel


class Answer(BaseModel):
    session_id: str
    question_id: str
    selected_answer: int
