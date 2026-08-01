import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# We'll use SQLite for local scaffolding if PostgreSQL URL is not provided
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    ai_source = Column(String, index=True)
    metadata_json = Column(Text)
    content = Column(Text)
    timestamp = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))

class SubWorker(Base):
    __tablename__ = "subworkers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String)
    task = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
