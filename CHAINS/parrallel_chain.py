from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-31B-it",
    task = "text-generation"
)

model1 = ChatHuggingFace(llm=llm)

model2 = ChatOpenAI()

parser = StrOutputParser()



prompt1 = PromptTemplate(
    template='Generate short and simple notes from the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate 5 questions from the following {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes --> {notes} and quiz --> {quiz}.',
    input_variables=['notes', 'quiz']
)


parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text =  """
        Standardized Tests provide an objective, efficient method for measuring student achievement and holding schools accountable, but they are criticized for narrowing the curriculum and creating inequity. 

        Pros:
        Objective Measurement: They offer consistent benchmarks and quick data analysis to track student progress and identify learning gaps across large populations. 
        Accountability: Results help policymakers allocate resources and evaluate teacher or school performance against national standards. 
        Efficiency: Automated scoring allows for the rapid assessment of large numbers of students, making them cost-effective for education systems. 

        Cons:
        Limited Scope: Tests often ignore creative thinking, problem-solving, and soft skills, leading to a narrow curriculum focused primarily on tested subjects like math and reading. 
        Inequity: Scores frequently reflect socioeconomic status and access to test preparation rather than true ability, disadvantaging marginalized groups. 

        Negative Impact: High-stakes testing can cause significant student anxiety and pressure educators to "teach to the test," reducing opportunities for deeper, engaging learning. 
        For a more comprehensive view of student capabilities, many educators advocate for alternative assessments such as portfolios and project-based learning, which better capture individual growth and practical skills. 
            
        """

result = chain.invoke({'text': text})

print(result)