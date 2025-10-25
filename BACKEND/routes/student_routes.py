from fastapi import APIRouter, Depends  
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/" , response_model=list[schemas.Student])
def get_students(db:Session = Depends(database.get_db)):
    return db.query(models.Student).all()