from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name : str = 'subham'
    age : Optional[int] = None
    cgpa : float = Field(gt=0, lt=10, description='This is CGPA of the student')
    
new_student = {
    'age' : 20,
    'cgpa' : 8.3
}

s1 = Student(**new_student)

s1_dict = dict(s1)

s1_json = s1.model_dump_json()