from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-31B-it",
    task = "text-generation"
)

model1 = ChatHuggingFace(llm=llm)

model2 = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following {topic}.',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='Generate five quiz from the following {text}.',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into single document notes-->{notes} and quize --> {quiz}',
    input_variables=['notes', 'quiz']   
)


parallel_chain = RunnableParallel(
    {
        'notes': prompt1 | model1 | parser,
        'quiz' : prompt2 | model2 | parser     
     
     }
)

merge_chain = prompt3 | model1 | parser 

final_chain = parallel_chain | merge_chain

result = final_chain.invoke()


# final_chain.get_graph.print_ascii