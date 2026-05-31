from langchain_community.document_loaders import  TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
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

prompt = PromptTemplate(
    template='Write the summary for the following {poem}.',
    input_variables=['poem']
)

loader = TextLoader('datasets/1661-0.txt', encoding = 'utf-8')
docs = loader.load()

chain = prompt | model | parser

result= chain.invoke({'poem': docs[0].page_content})
print(result)