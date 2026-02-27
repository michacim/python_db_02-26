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
        pass

    def get_user_by_credentails(self, username:str, password:str)->User:
        ''' user verify_password(...)
            Login: User holen, Passwort prüfen
               -> prüfe Parameter und werfe Exception (raise ValueError)
        '''
        pass