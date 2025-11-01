import myapp.signals # type: ignore
from pydantic import BaseModel, EmailStr #, Field, confloat, conint
from typing import Optional 
from datetime import datetime 

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    department: str
    year: int
    attendance: float
    gpa: float

class StudentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    department: Optional[str]
    year: Optional[int]
    attendance: Optional[float]
    gpa: Optional[float]


class StudentOut(StudentBase):
    id: int
    risk_score: float
    created_at: datetime
    updated_at: Optional[datetime]

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
