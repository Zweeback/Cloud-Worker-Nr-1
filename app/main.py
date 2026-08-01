from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from .database import get_db, ChatLog, SubWorker
from .gatekeeper import alice
import json

app = FastAPI(title="Alice - Cloud Worker Dashboard")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

class ChatIngest(BaseModel):
    ai_source: str
    metadata_json: dict
    content: str

class SubWorkerCreate(BaseModel):
    name: str
    task: str

@app.on_event("startup")
def startup_event():
    # Initialize some mock connectors on startup
    alice.manage_connectors("google_drive", "dummy_token")
    alice.manage_connectors("sql_db", "dummy_connection_string")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/subworkers")
def get_subworkers(db = Depends(get_db)):
    workers = db.query(SubWorker).all()
    return workers

@app.post("/api/subworkers")
def create_subworker(worker: SubWorkerCreate, db = Depends(get_db)):
    new_worker = alice.spawn_subworker(worker.name, worker.task, db)
    return new_worker

@app.get("/api/chats")
def get_chats(db = Depends(get_db)):
    chats = db.query(ChatLog).order_by(ChatLog.timestamp.desc()).all()
    return chats

@app.post("/api/chats")
def ingest_chat(chat: ChatIngest, db = Depends(get_db)):
    log = alice.ingest_ai_chat(chat.ai_source, chat.metadata_json, chat.content, db)
    return log

@app.get("/api/drive-search")
def drive_search(query: str = "3D glasses"):
    results = alice.search_google_drive(query)
    return results
