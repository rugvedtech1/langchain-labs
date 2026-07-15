# AI Chatbot — Backend (Project 1)

FastAPI backend with LangChain + OpenAI integration.

## Status: Core Complete (Backend MVP)

### Implemented
- FastAPI project structure (routes/services/schemas)
- LangChain chat model integration (OpenAI)
- Session-based conversation memory
- Streaming responses (Server-Sent Events)
- Unit tests (pytest, mocked LLM calls)
- GitHub Actions CI (automated test runs on push)

### Not implemented (deferred)
- Authentication (JWT)
- Docker containerization
- CD / automated deployment
- Frontend UI

## Run locally
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Add `OPENAI_API_KEY` to `.env`
5. `uvicorn main:app --reload`

## Endpoints
- `GET /health`
- `POST /api/chat` — single request/response
- `POST /api/chat/stream` — streaming (SSE)
