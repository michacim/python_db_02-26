from database import Base, engine, session
from models import User
from crud import UserRepository


def main():
    Base.metadata.create_all(engine) # Create Table if not exists

    repo = UserRepository(session)

    repo.create_user(User(name="ina",email="ina@web.de"))
    users = repo.find_all_users()
    print(users)
    
if __name__=="__main__":
    main()