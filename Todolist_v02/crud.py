# python imports
from sqlalchemy.orm import Session
from sqlalchemy import text
# custom imports
from models import Todo, User
from util import hash_password, verify_password

class TodoRepository:
    def __init__(self, session:Session):
        self.session= session

    def create(self,todo:Todo)-> Todo:
        """ 
        
        """
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo
    def find_all_todo_by_userid(self, user_id:int)-> list[Todo]:
        return (
            self.session.query(Todo)
            .filter(Todo.id==user_id)
            .order_by(Todo.deadline.asc().nulls_last(), Todo.id.asc())
            .all()
        )
        

    def find_open_todos(self,user_id:int)->list[Todo]:
        return (
            self.session.query(Todo)
            .filter(Todo.user_id == user_id,
                    Todo.state == "OPEN"
            ) #TODO OPEN or NOT DONE
            .all()

        )

    def find_todos_by_task(self,user_id:int, task:str )->list[Todo]:
        return (
            self.session.query(Todo)
            .filter(
                Todo.user_id ==user_id,
                Todo.task.ilike(f"%{task}%") 
            )
            .all()
        )

    def update_todo_state(self, todo_id:int, new_state:str)-> Todo | None:
        allowed = {"OPEN","IN_PROGRESS","DONE"}
        if new_state not in allowed:
            raise ValueError("Invalid state")
        todo = self.session.query(Todo).filter(Todo.id==todo_id).first()
        if not todo:
            return None
        todo.state = new_state
        self.session.commit()
        self.session.refresh()
        return todo


    
class UserRepository:
    def __init__(self, session:Session):
        self.session= session
    def create(self,user:User)-> User:
 
        if user is None:
            raise ValueError("user darf nicht None sein")
        if not user.username:
            raise ValueError("username ist Pflicht")
        if not user.password:
            raise ValueError("password ist Pflicht")

        existing = self.session.query(User).filter(User.username == user.username).first()
        if existing:
            raise ValueError("username existiert bereits")

        user.password = hash_password(user.password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)  
        return user
    
    def get_user_by_credentails(self, username:str, password:str)->User | None:
            ''' user verify_password(...)
                Login: User holen, Passwort prüfen
                -> prüfe Parameter und werfe Exception (raise ValueError)
            '''
            if not username or not password:
                return None

            user = self.session.query(User).filter(User.username == username).first()
            if not user:
                return None

            return user if verify_password(password, user.password) else None