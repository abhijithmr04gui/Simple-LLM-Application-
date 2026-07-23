from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name:str 
    age : Optional[int] = None
    email : EmailStr 

new_student = {"name" : "Abhijith","age" : 21,"email" : "abhi@gmail.com"}

student = Student(**new_student)

print(student)