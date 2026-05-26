from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate(
    [
        ('system', 'You are expert in {domain}'),
        ('human', 'Explain in simple words, what is {topic}')
    ]
)

prompt = chat_template.invoke({'domain': 'engineer', 'topic': 'llms'})

print(prompt)
