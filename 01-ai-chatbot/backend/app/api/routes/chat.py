from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import get_chat_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    reply = get_chat_response(request.message, request.session_id)
    return ChatResponse(reply=reply)

from fastapi.responses import StreamingResponse
from app.services.chat_service import stream_chat_response

@router.post("/chat/stream")
def chat_stream(request: ChatRequest):
    return StreamingResponse(
        stream_chat_response(request.message, request.session_id),
        media_type="text/event-stream",
    )
