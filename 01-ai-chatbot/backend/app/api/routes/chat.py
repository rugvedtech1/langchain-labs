from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import get_chat_response

router=APIRouter()

@router.post("/chat",response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    reply = get_chat_response(request.message)
    return ChatResponse(reply=reply)