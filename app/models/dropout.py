from sqlalchemy import Column, Integer, Float, String
from app.db.base import Base

class DropoutPrediction(Base):
    __tablename__ = "dropout_predictions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    risk_score = Column(Float)
    status = Column(String)
