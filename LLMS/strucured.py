from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str 
    age : Optional[int] = None
    email : EmailStr 
    CGPA : float = Field(gt=0,lt=10)

new_student = {"name" : "Abhijith","age" : 21,"email" : "abhi@gmail.com","cgpa":9 }

student = Student(**new_student)

print(student)