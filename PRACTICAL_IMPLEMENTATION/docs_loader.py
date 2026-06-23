from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

# load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
# )

# model = ChatHuggingFace(llm=llm)


loader = TextLoader(file_path=r'C:\Users\Subham Pathak\Desktop\AI\LANGCHAIN\datasets\1661-0.txt', encoding='utf-8')

docs = loader.load()

# print(docs[0])
print(len(docs))