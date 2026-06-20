from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

paper_input = st.selectbox('Select Research Paper', ['Attention All you need', 'BERT: Pre-training of bidirectional transfomers', 'GPT-3: Language models are few short learners.'])
length_input = st.selectbox('Select the length', ['Short', 'Medium', 'Long', 'Points'])
overall_input = st.selectbox('Select the overall input',['SUmmary','Bullet Points','Brief'])

    
    

template = PromptTemplate(
    template="Write the {length_input} of {paper_input} in {overall_input}",
    input_variables=['length_input', 'paper_input', 'overall_input'] 
)    
    
chain = template | model
    
    
    
if st.button('Summarize'):
    chain = template | model
    
    result= chain.invoke({
        'length_input':length_input,
        'paper_input': paper_input,
        'overall_input':overall_input 
    })
    st.write(result.content)
        
    
    
    
    
    
    
    

    
# Why use PromptTemplate over f strings?

# 1. Default Validation.
# 2. Reusable
# 3. Langchain Ecosystem