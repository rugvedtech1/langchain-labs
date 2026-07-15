from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(model, get_session_history)

def get_chat_response(user_message: str, session_id: str) -> str:
    config = {"configurable": {"session_id": session_id}}
    response = chain_with_history.invoke(user_message, config=config)
    return response.content

def stream_chat_response(user_message: str, session_id: str):
    config = {"configurable": {"session_id": session_id}}
    for chunk in chain_with_history.stream(user_message, config=config):
        yield chunk.content
