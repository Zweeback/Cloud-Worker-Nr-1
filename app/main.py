from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

app = FastAPI(title="Autonomous Agent Gateway", description="Gatekeeper und Kontroll-Dashboard für 'Alice'.")

# Initialisiere den Agenten (Platzhalter für den vollen Gatekeeper)
# Beachte: Für echte LLM calls wird ein API Key benötigt (OPENAI_API_KEY)
llm = ChatOpenAI(temperature=0, model_name="gpt-4o", openai_api_key=os.getenv("OPENAI_API_KEY", "dummy"))

# Deutsches Prompt-Template für Alice
prompt_template = PromptTemplate.from_template(
    "Du bist Alice, ein autonomer Webagent und Daten-Manager. Antworte immer auf Deutsch. Aufgabe: {task}"
)

@app.get("/")
def read_root():
    """
    Dashboard Einstiegspunkt.
    Zeigt den Status des Gatekeepers und grundlegende Informationen.
    """
    return {"status": "online", "agent": "Alice", "message": "Gatekeeper ist aktiv."}

@app.get("/agent/status")
def get_agent_status():
    """
    Gibt den Status des LangChain Agenten zurück.
    """
    return {"llm_initialized": llm is not None, "model": llm.model_name}
