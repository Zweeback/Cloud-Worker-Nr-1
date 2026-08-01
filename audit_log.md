# Audit Log & Project Documentation: Cloud-Worker-Nr-1

## Project Goals & Overview
The goal is to develop an autonomous web agent gateway ("Alice") capable of acting as an omnipotent multiprofessional Cloud worker.
The agent must:
- Act as the main gatekeeper managing various AI sub-workers.
- Perform live monitoring, web searching, and data collection.
- Aggregate chat data from all AI sessions and store it along with metadata.
- Speak and document in German.
- Steer the patch/GitHub process and maintain project structure in Codespaces.
- Access external resources, Google Drive ("3D glasses"), web browsers, etc.

## Technical Architecture & Stack
- **Backend/Dashboard:** FastAPI, Uvicorn, Python
- **Agent Framework:** LangChain, OpenAI
- **Database:** PostgreSQL (with SQLAlchemy/psycopg2) and dynamic data storage, falling back to SQLite for local scaffolding.
- **Frontend GUI:** HTML/JS, designed to be sense-making like Poe for control and management.
- **Connectors:** Google Drive API, web search connectors, and remote resource connectors.
- **Integrations:** MCP calls to Render (list_workspaces, list_services, list_postgres_instances).

## Project Plan
1. Initialize Project Structure: Set up Python environment. Create `app`, `app/static`, `app/templates` directories.
2. Setup Dependencies: Create `requirements.txt` (FastAPI, uvicorn, langchain, openai, sqlalchemy, psycopg2, google-api-python-client).
3. Database Integration: Implement PostgreSQL connection (fallback to SQLite).
4. Agent Gateway & Connectors: Create gatekeeper "Alice". Implement scaffold connectors for Drive and web search.
5. Dashboard Interface: Build FastAPI web dashboard and frontend GUI.
6. German Capability: Ensure system prompts instruct in German.

## External Resources
- **Server Name:** lemehost.com V2 (France KVM)
- **OS:** Ubuntu 24.04
- **IP Address:** 51.68.66.146
- **SSH Port:** 22
- **Note:** Security practice enforced: password is omitted from documentation.

## Current Audit Status
- Initialization phase started.
