# Importing the dependecies

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)


model = ChatHuggingFace(llm=llm)


messages = [
    SystemMessage(content='You are an AI expert'),
    HumanMessage(content='Tell me about langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))
print(messages)