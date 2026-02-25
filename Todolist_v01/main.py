from database import Base, engine, session
from models import User, Todo
from crud import UserRepository, TodoRepository
from datetime import date


def  main():
    Base.metadata.create_all(engine)
    user_repo = UserRepository(session)
    todo_repo = TodoRepository(session)

    u1 = User(username="max",password="12345")
    create_user1 =   user_repo.create(u1)
    create_user1.todos.append( Todo(task="einkaufen",description="Miclh und Brot",deadline=date(2026,2,26)) )
                              
    print(create_user1)




if __name__=="__main__":
    main()