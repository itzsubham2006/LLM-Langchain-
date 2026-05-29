from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-31B-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()


prompt1 = PromptTemplate(
    template='Write a joke on {topic}.',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='Write the explaination of the joke {joke}',
    input_variables=['joke']
)

passthrough = RunnablePassthrough()

joke_gen = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})

print(result)