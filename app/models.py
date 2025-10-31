from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# -------------------- User Model --------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to learning data
    study_sessions = relationship("StudySession", back_populates="user", cascade="all, delete-orphan")


# -------------------- StudySession Model --------------------
class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    topic = Column(String(150), nullable=False)
    subtopic = Column(String(150), nullable=True)
    last_studied = Column(DateTime, default=datetime.utcnow)
    next_review = Column(DateTime, nullable=True)
    difficulty = Column(Integer, default=1)  # 1 to 5
    remembered = Column(Boolean, default=False)

    user = relationship("User", back_populates="study_sessions")
