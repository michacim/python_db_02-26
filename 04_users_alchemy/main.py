from database import Base, engine, session
from models import User
from crud import UserRepository


def main():
    Base.metadata.create_all(engine) # Create Table if not exists

    repo = UserRepository(session)

   # repo.create_user(User(name="otto",email="otto@web.de"))
    users = repo.find_all_users()   
    print(users)

    user= repo.update_user(User(id=1,name="ina",email="ina@gmail.com"))
    print("update:", user)

    print (repo.find_user_by_name("ina"))
 
    
if __name__=="__main__":
    main()