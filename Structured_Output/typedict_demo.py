from typing import TypedDict

class Person(TypedDict):
    
    name : str
    age : int
    
    
new_Person : Person = {
    'name': 'Subham',
    'age' : 20
}

print(new_Person)