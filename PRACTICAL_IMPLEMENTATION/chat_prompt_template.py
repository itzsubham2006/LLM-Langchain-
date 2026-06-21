from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)


model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate.from_messages([
    
        ('system', 'You are a helpful {domain} expert.'),
        ('human', 'Explain in simple terms what is {topic}.')
        
        ])

prompt = chat_template.invoke({
    'domain' : 'Software engineering',
    'topic' : 'Backend System'
}
)

print(prompt)