from typing import TypedDict

class Person(TypedDict):
    name: str
    age : int 
    gender : str

person_1 = Person(name = "Abhijith",age =21,gender = "Male")

print(person_1)
