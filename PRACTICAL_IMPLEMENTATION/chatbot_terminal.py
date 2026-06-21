from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

load_dotenv()

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content='Hello')
]

while(True):
    
    user_input = input("You: ")
    if user_input == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))
    
    result = model.invoke(user_input)
    
    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")
    
   
print(chat_history)