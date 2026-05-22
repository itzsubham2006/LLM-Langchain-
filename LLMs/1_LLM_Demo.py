from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

question = "Who is the prime minister of India"

result = llm.invoke(question)

print(result)

