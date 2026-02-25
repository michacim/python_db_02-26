# Todolist
## Version 0.1


## Model

* Todo
  * id: int (PK)
  * task: String
  * description: String/ Text
  * deadline: Date
  * state: Enum(OPEN,IN_PROGRESS, DONE)
  * Optional: PRIORITÄT 

* User
  * username
  * password
  * todos:List
  

## Datenbank
* SQlite
* ?

## Install
pip install sqlalchemy
pip install pymysql

## Aufgabe
  def find_all_todo_by_userid(self, user_id:int)-> list[Todo]:
          
  def find_open_todos(self,user_id:int)->list[Todo]:
        

  def find_todos_by_task(self,user_id:int, task:str )->list[Todo]:
        
  def update_todo_state(self, todo_id:int, new_state:str)-> Todo:

  teste in der Main
