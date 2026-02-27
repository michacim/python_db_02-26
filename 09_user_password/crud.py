from database import Session
from models import User
from util import hash_password, verify_password

class UserRepository:

    def __init__(self, session):
        self.session=session

    
    def create_user(self,user:User) ->User:
        ''' use hash_password(...)
        
            Speichert User mit gehashtem Passwort
               -> prüfe Parameter und werfe Exception (raise ValueError)
        '''
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