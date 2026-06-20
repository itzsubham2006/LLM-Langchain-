from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st
import random

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

st.header('Chatbot')
st.write('Hello this is a bot made by Subham, how can i help you?')



while(True):
    
    user_input = st.text_input('You')
    
    result = model.invoke(user_input)
    
    st.write(result.content)
