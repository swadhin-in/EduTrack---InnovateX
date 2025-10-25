from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    gender: str
    attendance: float
    grade: float


class StudentCreate(StudentBase):   
     pass

class Student(StudentBase):
    id: int
    is_active: bool
    dropout_risk: bool

    class Config:
        orm_mode = True
