class Person:
    def __init__(self, id:int, name:str, email:str = None):
        self._id = id
        self._name = name
        self._email = email

    
    def __repr__(self): # toString
        return f"Person(id={self._id}, name={self._name}, email={self._email})"
    
    @property #lesen
    def id(self)->int:
        return self._id
    

    @id.setter #schreiben
    def id(self,id):
        self._id=id

    
    @property #lesen
    def name(self)->str:
        
        return self._name
    
    
    @name.setter #schreiben
    def name(self,name):

        self._name=name


# Variante 2 -@dataclass
from dataclasses import dataclass
from datetime import date
@dataclass
class Kurs:
    id: int
    name: str
    start: date | None = None
    teacher: str = ""
    weeks: int =4




