from dataclasses import  dataclass

@dataclass
class Book:
    id:int | None = None 
    title:str=""
    author:str=""
    genre:str=""
    published_year:int=0