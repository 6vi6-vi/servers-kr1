from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User
from pydantic import BaseModel

app = FastAPI()
user = User(name = "Валерия Иванова", id = 1)
feedbacks = []

class Feedback(BaseModel):
    name: str
    message: str

@app.get("/")
async def html():
    return FileResponse("index.html")

@app.get("/users")
async def get_user():
    return user

@app.post("/feedback")
async def post_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}