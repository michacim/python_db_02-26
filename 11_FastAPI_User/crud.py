from sqlalchemy.orm import Session
from models import User


class UserRepository:
    def __init__(self,session:Session):
        self.session = session

    def create_user(self, user:User) ->User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user


    def get_all_users(self)->list[User]:
        return self.session.query(User).all()
    
    def get_user_by_email(self, email:str)->User:
        return self.session.query(User).filter(User.email==email).first()