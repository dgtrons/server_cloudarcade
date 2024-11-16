def individual_serial(question) -> dict:
    return {
        "id": str(question["_id"]),
        "question": question["question"],
        "choices": question["choices"],
        "answer": question["answer"],
        "key": question["key"]
    }


def list_serial(questions) -> list:
    return [individual_serial(question) for question in questions]
