from fastapi import APIRouter, HTTPException
from models.questions import Question
from models.answers import Answer
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET request method
@router.get("/")
async def get_questions():
    questions = collection_name.find()
    return list_serial(questions)


# POST request method IF NEEDED?
@router.post("/")
async def create_question(question: Question):
    question = dict(question)
    collection_name.insert_one(question)


# PUT request method. EN el ejemplo se modificaba el valor de un to do
@router.put("/{id}")
async def put_question(id: str, question: Question):
    collection_name.find_one_and_update({"_id": ObjectId(id)},
                                        {"$set": dict(question)})


# submit values
@router.post("/submit")
async def submit_answers(answers: list[Answer]):
    score = 0
    for answer in answers:
        question = await collection_name.find_one({"_id": answer.question_id})
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        if question["correct_answer"] == answer.selected_answer:
            score += 1
    return {"score": score}
