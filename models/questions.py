from pydantic import BaseModel


class Question(BaseModel):
    question: str
    choices: list[str]
    answer: int
    key: int

    def __str__(self):
        return f"{self.question} {self.answer}"
