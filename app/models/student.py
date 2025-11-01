# type: ignore
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    attendance = Column(Float, nullable=False, default=100.0)  # percentage 0.0 - 100.0
    gpa = Column(Float, nullable=False, default=4.0)  # 0.0 - 4.0 scale
    risk_score = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())