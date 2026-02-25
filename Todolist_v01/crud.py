# python imports
from sqlalchemy.orm import Session
from sqlalchemy import text
# custom imports
from models import Todo, User

class TodoRepository:
    def __init__(self, session:Session):
        self.session= session

    def create(self,todo:Todo)-> Todo:
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo
    def find_all_todo_by_userid(self, user_id:int)-> list[Todo]:
        pass

    def find_open_todos(self,user_id:int)->list[Todo]:
        pass

    def find_todos_by_task(self,user_id:int, task:str )->list[Todo]:
        pass

    def update_todo_state(self, todo_id:int, new_state:str)-> Todo:
        pass

    
class UserRepository:
    def __init__(self, session:Session):
        self.session= session
    def create(self,user:User)-> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user