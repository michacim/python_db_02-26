from models import User
from sqlalchemy.orm import Session



class UserRepository:

    def __init__(self,session:Session):
        self.session =session


    def create_user(self,user:User)->User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def find_all_users(self):
        return self.session.query(User).all()