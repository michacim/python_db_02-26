from database import Base, engine, session
from models import User
from crud import UserRepository


def main():
    ## Test
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    repo = UserRepository(session)

    u = User(username="micha",password="geheim123")
    repo.create_user(u)

    logged_in = repo.get_user_by_credentails("micha","geheim123")
    print("Login ok",logged_in)

if __name__=="__main__":
    main()

