from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
# Routes /Endpoint
#!!!!!!!!!!!!!!!!!!! start: uvicorn main:app --reload !!!!!!!!!!!!!!!!!!!!!!
class Item(BaseModel):
    name:str
    price:float
    description: str | None =None


@app.get("/") # http://127.0.0.1:8000
def get_root():
    return {"message":"Hello Rest    "}


# Path-Parameter und Query-Parameter
@app.get("/items/{item_id}")   # http://localhost:8000/items/12?q=Hallo
def get_item(item_id:int, q:str =None):
    return {"item_id":item_id,  "query":q} 

@app.post("/items")
def create_item(item:Item):
    return {"message":"Item erzeugt", "item":item }

@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return {"message":f"Item {item_id} aktualisiert", "item":item }
 
@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {"message":f"Item {item_id} gelöscht" }