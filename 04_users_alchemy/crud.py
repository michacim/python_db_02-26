from models import User
from sqlalchemy.orm import Session
from sqlalchemy import text, select, update


class UserRepository:
    def __init__(self, session:Session):
        self.session=session

    def create_user(self,user:User)-> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def find_all_users(self)->list[User]:
        return self.session.query(User).all()
    
    def find_user_by_id(self, id:int)->User:
        return self.session.query(User).filter(User.id==id).first()
    
    def delete_user_by_id(self,id:int)-> User:
        user = self.session.query(User).filter(User.id==id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
        return user
    
    def update_user(self, user:User) -> User | None:
        db_user = self.session.get(User,user.id)
        if not db_user:
            return None
        
        if user.name is not None:
            db_user.name = user.name
        if user.email is not None:
            db_user.email = user.email

        self.session.commit()
        self.session.refresh(db_user)
        return db_user    
    

    def find_user_by_name(self,name:str)->list[User]:
        stmt = text("select * from user where name like :name") # Native SQL (Datenbankabhängig)
        return self.session.execute(stmt,{"name":f"%{name}%"}).fetchall()
    
    
    def find_user_by_name2(self,name:str)->list[User]:
        stmt = select(User).where(User.name.ilike(f"%{name}%"))
        return self.session.execute(stmt).scalars().all()
