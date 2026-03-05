# Todolist
## Version 0.3

### Version mit Datenbank(SQLAlchemy) und Rest (FastAPI)
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
* Todo-Projekt soll mit rest funktionieren (erstmal nur create(get_all))
* schemas.py implementieren (evtl. estmal nur die wichtigesten)
* routers.py implementieren (evtl. ertmal nur create_user)