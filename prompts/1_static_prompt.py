from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

llm = HuggingFaceEndpoint( repo_id = "deepseek-ai/DeepSeek-V4-Flash",
    task = "text-generation")

model = ChatHuggingFace(llm=llm)


st.header("Text summarize tool")
user_input = st.text_input("Enter your prompt: ")

if st.button('Summarize'):
    result=model.invoke(user_input)  
    st.write(result.content)
    
    
    
    
    
#     llm = HuggingFaceEndpoint(
#     repo_id = "google/gemma-4-31B-it",
#     task = "text-generation"
# )