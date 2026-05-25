from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=30)

text = "Hello how are you"

document = [
    'This is subham practicing Gen AI',
    'Northeast is the best',
    'The weather is cloudy today.'
]


document_query= embedding.embed_documents(document)
text_query = embedding.embed_query(text)

similarity = cosine_similarity([document_query], text_query) #both the parameters must be in 2d list/array/vector

print(similarity)