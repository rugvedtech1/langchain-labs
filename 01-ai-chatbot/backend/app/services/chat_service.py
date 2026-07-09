from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

def get_chat_response(user_message:str)->str:
    response=model.invoke(user_message)
    return response.content