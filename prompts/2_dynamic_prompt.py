from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)


st.header('Mini-pt')
paper_input = st.selectbox('Select the paper you want', ['Attention all you need', 'BERT: Bidirectional Transformers', 'GPT: Language Models are few-short learners', 'Diffusions models beats GANs on image Synthesis',  'Describe yourself'])

len_input = st.selectbox('Enter the length of the output', ['SHORT: (5-50) Words', 'MEDIUM: (50-80) words', 'LARGE: (100-200)+ words',  'Describe yourself'])

style_input = st.selectbox('Select the style of the output', ['Paragraphs','Small paragraphs', 'Bullet-points', 'Describe yourself'])


# Creating the custom prompt------------>
template = PromptTemplate(
    template=
"""
You are an expert academic writer and formatter.

Generate a {style_input} style answer for the following paper/question.

Question/Paper:
{paper_input}

Requirements:
- The answer length should be approximately {len_input}.
- Maintain a clean, human-written style.
- Use simple but effective language.
- Keep the structure organized with proper paragraphs and headings if needed.
- Avoid unnecessary repetition.
- Make the response accurate, natural, and exam-friendly.
- If the question requires examples, include relevant examples.
- If definitions are asked, make them concise and clear.
- If the question is theoretical, explain step-by-step in an understandable way.

Output only the final answer without extra explanations.
    
"""
, input_variables=['style_input', 'paper_input', 'len_input'],
validate_template=False
    
)



# template = load_prompt('./template.json')

# Filing the placeholders---------->

# ------------------------------>
if st.button('Click here'):
    
    chain = template | model
    
    result = chain.invoke(
    { 
    'paper_input': paper_input,
    'style_input': style_input,
    'len_input': len_input  
    }
)
    st.write(result.content)
    
    
    
    
# Why use PromptTemplate over f strings?

# 1. Default Validation.
# 2. Reusable
# 3. Langchain Ecosystem