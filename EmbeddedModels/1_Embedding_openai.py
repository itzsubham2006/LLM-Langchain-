from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=30)

result= embedding.embed_query("Hello Hi are you")

print(result) # It will throw an error because API key is not passed, since we have to buy the API key