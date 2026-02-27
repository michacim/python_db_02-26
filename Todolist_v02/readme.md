# Todolist
## Version 0.2


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
* Todolist soll mit Login uns Passwortverschlüsselung funktionieren
* crud: create anpassen
* crud ergänzen: def get_user_by_credentails(self, username:str, password:str)->User | None: 
* Optional: schreibe einen Unittest für create und get_user_by_credentails
* util.py integrieren