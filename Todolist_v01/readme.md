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