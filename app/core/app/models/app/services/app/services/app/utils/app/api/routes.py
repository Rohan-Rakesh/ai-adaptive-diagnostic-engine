from fastapi import APIRouter
from bson import ObjectId
from app.core.database import questions_collection, sessions_collection
from app.services.adaptive_engine import update_ability, select_next_question
from app.services.ai_service import generate_study_plan
from app.utils.helpers import serialize_doc
from app.models.schemas import AnswerSubmission

router = APIRouter()


@router.post("/start-session")
def start_session():

    session = {
        "ability_score": 0.5,
        "history": [],
        "questions_answered": 0
    }

    result = sessions_collection.insert_one(session)

    return {"session_id": str(result.inserted_id)}


@router.get("/next-question")
def next_question(session_id: str):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    ability = session["ability_score"]

    questions = list(questions_collection.find())

    question = select_next_question(ability, questions)

    return serialize_doc(question)


@router.post("/submit-answer")
def submit_answer(payload: AnswerSubmission):

    question = questions_collection.find_one(
        {"_id": ObjectId(payload.question_id)}
    )

    session = sessions_collection.find_one(
        {"_id": ObjectId(payload.session_id)}
    )

    correct = payload.answer == question["correct_answer"]

    new_ability = update_ability(
        session["ability_score"],
        question["difficulty"],
        correct
    )

    sessions_collection.update_one(
        {"_id": ObjectId(payload.session_id)},
        {"$set": {"ability_score": new_ability}}
    )

    return {
        "correct": correct,
        "new_ability": new_ability
    }


@router.get("/study-plan")
def study_plan(session_id: str):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    missed_topics = []

    for h in session.get("history", []):
        if not h["correct"]:
            missed_topics.append(h["topic"])

    plan = generate_study_plan(missed_topics)

    return {"study_plan": plan}
