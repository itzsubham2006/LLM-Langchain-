from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    
    summary : Annotated[str, 'Returns summary of the Review']
    sentiments : Annotated[str, 'Returns sentiments of the review']
    
structured_output_model = model.with_structured_output(Review)

result = structured_output_model.invoke("""Standardized Tests provide an objective, efficient method for measuring student achievement and holding schools accountable, but they are criticized for narrowing the curriculum and creating inequity. 

Pros:
    Objective Measurement: They offer consistent benchmarks and quick data analysis to track student progress and identify learning gaps across large populations. 
    Accountability: Results help policymakers allocate resources and evaluate teacher or school performance against national standards. 
    Efficiency: Automated scoring allows for the rapid assessment of large numbers of students, making them cost-effective for education systems. 

Cons:
    Limited Scope: Tests often ignore creative thinking, problem-solving, and soft skills, leading to a narrow curriculum focused primarily on tested subjects like math and reading. 
    Inequity: Scores frequently reflect socioeconomic status and access to test preparation rather than true ability, disadvantaging marginalized groups. 

Negative Impact: High-stakes testing can cause significant student anxiety and pressure educators to "teach to the test," reducing opportunities for deeper, engaging learning. 
For a more comprehensive view of student capabilities, many educators advocate for alternative assessments such as portfolios and project-based learning, which better capture individual growth and practical skills. """)


print(result)