from fastapi import FastAPI
from .import models, database
from .routes import student_routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Student Management System", version="1.0.0")

app.include_router(student_routes.router)

@app.get( "/")
def home():
    return {"message": "Welcome to Dropout Management System API"}