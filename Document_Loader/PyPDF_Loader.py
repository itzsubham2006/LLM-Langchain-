from langchain_community.document_loaders import PyPDFLoader
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
    template='Write the summary of the {document}',
    input_variables=['document']
)

loader = PyPDFLoader(
    file_path=r'C:\Users\Subham Pathak\Documents\ACADEMICS\NOTES\COA\COA_BOOKS'
    
)

document = loader.load()
chain = model | prompt | parser

result = chain.invoke({'document': document[0].page_content})
print(result)