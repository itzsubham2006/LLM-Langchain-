# In langchain Structured Output refers to the practice of having language model return response in a 
# well defined data format (example-> JSON), rather than free form text. This makes the model easier to parse
# and work with programitaclly



# LLMs which have capability to give structured output, in that situation we can use (with_structured_output) class, and which cannot give (Output_parser) class


# Three ways to format in structured way-------> 1) TypedDict 2) Pydantic  3) JSON_Schema


# ----------------------------------------------------------------------------------------------------------------------------------------------

# 1. TypedDict

# TypedDict is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.

# Why use TypedDict?


# It tells Python what keys are required and what types of values they should have.

# It does not validate data at runtime (it just helps with type hints for better coding).


from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from pydantic import BaseModel,  Field
from typing import Literal, Optional

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

#Schema
class Review(BaseModel):
    
    summary : str = Field(description='This is the summary of the review')
    pros : Optional[list[str]] = Field(description='This is pros of the review')
    cons : Optional[list[str]] = Field(description='This is cons of the review')
    sentiments : Literal['pros', 'cons' ] = Field(description="Tell whether the review is good or bad")
    name : Optional[str] = Field(description='Give the name of the person who wrote this review')
    
    
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Standardized Tests provide an objective, efficient method for measuring student achievement and holding schools accountable, but they are criticized for narrowing the curriculum and creating inequity. 

Pros:
Objective Measurement: They offer consistent benchmarks and quick data analysis to track student progress and identify learning gaps across large populations. 
Accountability: Results help policymakers allocate resources and evaluate teacher or school performance against national standards. 
Efficiency: Automated scoring allows for the rapid assessment of large numbers of students, making them cost-effective for education systems. 

Cons:
Limited Scope: Tests often ignore creative thinking, problem-solving, and soft skills, leading to a narrow curriculum focused primarily on tested subjects like math and reading. 
Inequity: Scores frequently reflect socioeconomic status and access to test preparation rather than true ability, disadvantaging marginalized groups. 

Negative Impact: High-stakes testing can cause significant student anxiety and pressure educators to "teach to the test," reducing opportunities for deeper, engaging learning. 
For a more comprehensive view of student capabilities, many educators advocate for alternative assessments such as portfolios and project-based learning, which better capture individual growth and practical skills.

By Subham Pathak

""")

print(result)

