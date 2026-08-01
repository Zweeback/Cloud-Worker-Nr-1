import json
from .database import SessionLocal, ChatLog, SubWorker

class Gatekeeper:
    """
    Main Alice Gatekeeper. Coordinates subworkers, manages connectors,
    and handles AI chat ingestion.
    """
    def __init__(self):
        self.connectors = {}
        self.subworkers = []

    def manage_connectors(self, name, credentials):
        """Mock method to manage connectors like Google Drive, SQL DB"""
        self.connectors[name] = "Connected"
        print(f"Connector {name} managed and connected.")
        return True

    def spawn_subworker(self, name, task):
        """Spawn a subworker for live-monitoring or web-search"""
        db = SessionLocal()
        new_worker = SubWorker(name=name, status="Running", task=task)
        db.add(new_worker)
        db.commit()
        db.refresh(new_worker)
        self.subworkers.append(new_worker)
        print(f"Spawned subworker {name} for task: {task}")
        db.close()
        return new_worker

    def search_google_drive(self, query="3D glasses"):
        """Mock search Google Drive"""
        if "google_drive" not in self.connectors:
            return {"error": "Google Drive connector not initialized"}
        # Mocking the response
        return [
            {"file": "3D_Glasses_Blueprints.pdf", "type": "pdf"},
            {"file": "Order_3D_Glasses_2023.xlsx", "type": "spreadsheet"}
        ]

    def ingest_ai_chat(self, ai_source, metadata, content):
        """Collect chat data from an AI to build the database"""
        db = SessionLocal()
        chat_log = ChatLog(
            ai_source=ai_source,
            metadata_json=json.dumps(metadata),
            content=content
        )
        db.add(chat_log)
        db.commit()
        db.refresh(chat_log)
        db.close()
        print(f"Ingested chat from {ai_source}")
        return chat_log

alice = Gatekeeper()
