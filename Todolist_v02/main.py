from database import Base, engine, session
from models import User, Todo
from crud import UserRepository, TodoRepository
from datetime import date


def  main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    user_repo = UserRepository(session)
    todo_repo = TodoRepository(session)

    u1 = User(username="max",password="12345")
    u1.todos.append( Todo(task="einkaufen",description="Milch und Brot",deadline=date(2026,2,26)) )

    create_user1 =   user_repo.create(u1)

    logged_in = user_repo.get_user_by_credentails("max","12345")
    if(logged_in is not None): print("Login ok",logged_in)

                              
    print(len(create_user1.todos))




if __name__=="__main__":
    main()