from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

history = []
while(True):
    
    user_input = input('You: ')
    history.append(user_input)
    
    if user_input == 'exit':
        break
   
    result = model.invoke(user_input)
    history.append(result.content)

    print(f'AI: {result.content}')
    
    
print('\n\nThe chat is ended\n\n\n')
user=input('Do u want to show the chat history (y/n)? ')

if(user=='y'):
    print(history)
