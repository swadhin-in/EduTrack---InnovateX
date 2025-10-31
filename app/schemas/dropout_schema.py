from pydantic import BaseModel

class DropoutPredictionBase(BaseModel):
    student_id: int
    risk_score: float
    status: str

class DropoutPredictionCreate(DropoutPredictionBase):
    pass

class DropoutPrediction(DropoutPredictionBase):
    id: int

    class Config:
        orm_mode = True
