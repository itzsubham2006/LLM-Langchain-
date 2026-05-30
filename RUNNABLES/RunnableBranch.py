# used for conditional statements
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-31B-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write the detailed explaination of {topic}.',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write the summary of the {text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()    
)
final_chain = RunnableSequence(report_gen_chain, branch_chain)
result = final_chain.invoke({'topic': 'AI'})
print(result)