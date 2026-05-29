from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-31B-it",
    task = "text-generation"
)


prompt1 = PromptTemplate(
    template='Write a detailed explaination about {topic}',
    input_variables=['topic', 'length']
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Summarize the following {text} in points',
    input_variables=['text']
)



chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result= chain.invoke(
    {
        'topic': 'AI'
        
    }
    
    )

print(result)