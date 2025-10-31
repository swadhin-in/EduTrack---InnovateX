from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.dropout_schema import DropoutPrediction, DropoutPredictionCreate
from app.models.dropout import DropoutPrediction as DropoutModel
from app.services.prediction_service import predict_dropout_risk
from app.db.session import SessionLocal

router = APIRouter(prefix="/dropout", tags=["Dropout"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/predict", response_model=DropoutPrediction)
def predict_dropout(data: DropoutPredictionCreate, db: Session = Depends(get_db)):
    # Simple placeholder logic
    data.risk_score = predict_dropout_risk(data.student_id)
    db_data = DropoutModel(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data
