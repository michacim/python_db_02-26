from database import session,Base, engine
from models import User,Address
from crud import UserRepository

def main():
    Base.metadata.create_all(engine)
    repo = UserRepository(session)

    address= Address(street="Teststr 3",postal_code="12345",city="Berlin")
    user = User(name="Max",email="max@web.de")

    user.addresses.append(address)

    repo.create_user(user)

    users = repo.find_all_users()
    print(users)

if __name__=="__main__":
    main()