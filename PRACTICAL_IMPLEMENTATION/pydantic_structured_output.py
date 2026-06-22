from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from pydantic import BaseModel,  Field
from typing import Literal, Optional

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "deepseek-ai/DeepSeek-V4-Flash", task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)


class Review(BaseModel):
    
    summary : Optional[str] = Field(description='This is the summary of the review.')
    pros_or_cons : Optional[list[str]]