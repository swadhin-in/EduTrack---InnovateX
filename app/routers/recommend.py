from fastapi import APIRouter
from app.services.recommendation_service import recommend_next_topic

router = APIRouter(prefix="/recommend", tags=["Recommendation"])

@router.get("/{student_id}")
def recommend_for_student(student_id: int):
    recommendation = recommend_next_topic(student_id)
    return {"student_id": student_id, "recommendation": recommendation}
