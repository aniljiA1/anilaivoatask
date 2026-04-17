from fastapi import FastAPI
from agent.graph import graph
from db.database import Base, engine
from pydantic import BaseModel
from agent.tools import ai_chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class LogRequest(BaseModel):
    doctor: str
    notes: str


@app.get("/")
def home():
    return {"message": "AI CRM Backend Running"}


# ✅ Chat → LangGraph

@app.post("/chat")
def chat(req: ChatRequest):
    return ai_chat({"message": req.message})


# ✅ Form Logging
@app.post("/log")
async def log(req: LogRequest):
    result = graph.invoke({
        "input": f"log interaction with {req.doctor}: {req.notes}"
    })
    return result