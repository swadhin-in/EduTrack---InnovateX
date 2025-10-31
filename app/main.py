from fastapi import FastAPI
from app.routers import auth, students, dropout, recommend
from app.db.session import engine
from app.models import user, student, dropout as dropout_model
from app.db.base import Base
from app.models.student import Student
Base.metadata.create_all(bind=engine)

user.Base.metadata.create_all(bind=engine)
student.Base.metadata.create_all(bind=engine)
dropout_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="EduTrack Backend API")
app.include_router(students.router, prefix="/api")

from .routers import study

app.include_router(study.router)


# Routers
app.include_router(auth.router)
app.include_router(students.router)
app.include_router(dropout.router)
app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "Welcome to EduTrack Backend API!"}

from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

