# What is Output Parser..??

# Output parser in langchain help convert raw LLM rsponses into structured formats like JSON, CSV, Pydantic models, and more, They ensure consistency, validation and ease of use in application. 1) StringOutput parser 2) JsonOutput Parser 3) Structured Output parser 4) Pydantic Output parser. 


# 1) StrOutputParser --> It is a simple output parser, which return simple strings.


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V4-Flash",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)       
# This is a open-source llm which doesnot return Structured output parser as default

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'black hole'})
result= model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})
result2 = model.invoke(prompt2)

print(result2.content)