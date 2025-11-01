# app/services/student_service.py
# type: ignore
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from app.models.student import Student
from app.schemas.student_schema import StudentCreate, StudentUpdate
from app.risk_engine import calculate_risk

def create_student(db: Session, payload: StudentCreate) -> Student:
    # calculate risk before saving
    risk = calculate_risk(payload.attendance, payload.gpa)
    db_student = Student(
        name=payload.name,
        email=payload.email,
        department=payload.department or None,
        year=payload.year or None,
        attendance=payload.attendance,
        gpa=payload.gpa,
        risk_score=risk,
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int) -> Optional[Student]:
    return db.query(Student).filter(Student.id == student_id).first()

def get_students(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    filters: Optional[Dict[str, Any]] = None,
) -> List[Student]:
    q = db.query(Student)
    if filters:
        if "department" in filters and filters["department"]:
            q = q.filter(Student.department == filters["department"])
        if "year" in filters and filters["year"] is not None:
            q = q.filter(Student.year == filters["year"])
        if "min_attendance" in filters and filters["min_attendance"] is not None:
            q = q.filter(Student.attendance >= filters["min_attendance"])
        if "max_attendance" in filters and filters["max_attendance"] is not None:
            q = q.filter(Student.attendance <= filters["max_attendance"])
        if "at_risk" in filters and filters["at_risk"] is True:
            q = q.filter(Student.risk_score >= filters.get("risk_threshold", 50.0))
    q = q.offset(skip).limit(limit)
    return q.all()

def update_student(db: Session, student_id: int, payload: StudentUpdate) -> Optional[Student]:
    student = get_student(db, student_id)
    if not student:
        return None
    # apply fields that are provided
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(student, field, value)
    # recalculate risk if attendance or gpa changed
    if "attendance" in payload.dict(exclude_unset=True) or "gpa" in payload.dict(exclude_unset=True):
        student.risk_score = calculate_risk(student.attendance, student.gpa)
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int) -> Optional[Student]:
    student = get_student(db, student_id)
    if not student:
        return None
    db.delete(student)
    db.commit()
    return student

def recalculate_risk(db: Session, student_id: int) -> Optional[Student]:
    student = get_student(db, student_id)
    if not student:
        return None
    student.risk_score = calculate_risk(student.attendance, student.gpa)
    db.commit()
    db.refresh(student)
    return student
