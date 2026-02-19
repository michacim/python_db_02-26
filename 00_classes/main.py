from models import Person, Kurs


def main():
    p1 = Person(1, "Ina","ina@web.de")
    p1.name="Otto"
    print(p1)
    print(p1.name)


    k1 = Kurs(1,"Python","2026-01-01","Ina",4)
    k2 = Kurs(id=2,name="Java")
    print(k1,k2)

if __name__ == "__main__":
    main()