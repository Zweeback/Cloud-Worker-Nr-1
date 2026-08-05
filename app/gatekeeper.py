import json
from .database import ChatLog, SubWorker

class Gatekeeper:
    """
    Main Alice Gatekeeper. Coordinates subworkers, manages connectors,
    and handles AI chat ingestion.
    """
    def __init__(self):
        self.connectors = {}

    def manage_connectors(self, name, credentials):
        """Mock method to manage connectors like Google Drive, SQL DB"""
        self.connectors[name] = "Connected"
        print(f"Connector {name} managed and connected.")
        return True

    def spawn_subworker(self, name, task, db):
        """Spawn a subworker for live-monitoring or web-search"""
        new_worker = SubWorker(name=name, status="Running", task=task)
        db.add(new_worker)
        db.commit()
        db.refresh(new_worker)
        print(f"Spawned subworker {name} for task: {task}")
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

    def ingest_ai_chat(self, ai_source, metadata, content, db):
        """Collect chat data from an AI to build the database"""
        chat_log = ChatLog(
            ai_source=ai_source,
            metadata_json=json.dumps(metadata),
            content=content
        )
        db.add(chat_log)
        db.commit()
        db.refresh(chat_log)
        print(f"Ingested chat from {ai_source}")
        return chat_log


    def generate_audio_for_chats(self, allowed_sources, db):
        """
        VETO-Pruefung: Nur erlaubte AI-Sources werden vertont.
        Simuliert die Erstellung von Fluester-Audio mit frz. Akzent fuer Alice.
        """
        if not allowed_sources:
            return []

        from .database import ChatLog
        chats = db.query(ChatLog).filter(ChatLog.ai_source.in_(allowed_sources)).filter(ChatLog.audio_file_path.is_(None)).all()
        processed = []
        for chat in chats:
            # Mock fuer TTS: Alice, frz. Akzent, fluesternd
            file_name = f"alice_whisper_fr_{chat.id}.mp3"
            chat.audio_file_path = f"/static/audio/{file_name}"
            processed.append(chat.id)

        db.commit()
        return processed

alice = Gatekeeper()
