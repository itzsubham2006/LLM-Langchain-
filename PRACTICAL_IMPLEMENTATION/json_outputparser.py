from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-31B-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Write a detailed explaination about {topic}.',
    input_variables=['topic']
)

template2 =  PromptTemplate(
    template='Write something that is very important in {detailed_explaination}',
    input_variables=['detailed_explanation'],
    partial_variables={'format_instructtion' : parser.get_format_instructions()}
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})
print(result)