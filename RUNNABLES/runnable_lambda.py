from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough
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
    template='Generate a joke about {topic}',
    input_variables=['topic']
)

# function to count the number of words
def count(text):
    return len(text.split())

gen_joke = RunnableSequence(prompt, model, parser)

parrallel_chain = RunnableParallel(
    {
        
    'joke' : RunnablePassthrough(),    
    'joke_count' : RunnableLambda(count),
}
)

final_chain = RunnableSequence(gen_joke, parrallel_chain)
result = final_chain.invoke({'topic': 'AI'})
print(result)