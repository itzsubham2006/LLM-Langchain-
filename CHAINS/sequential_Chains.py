from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-31B-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


template1 = PromptTemplate(
    template='Write a detailed information on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = 'write 5 main points on {text}',
    input_variables=['text']
    
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'cricket'})

print(result)


chain.get_graph().print_ascii() # it will print the chain structure