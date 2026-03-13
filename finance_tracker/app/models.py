#Aufgabe: ORM Tabellenstruktur

from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base


class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    category = Column(String, index=True)

    amount = Column(Float)

    date = Column(Date)



#| Feld     | Typ     | Zweck                        
#| -------- | ------- | --------------------------------- |
#| id       | Integer | eindeutiger Primärschlüssel       |
#| category | String  | Kategorie (z.B. Essen, Transport) |
#| amount   | Float   | Betrag                            |
#| date     | Date    | Datum der Ausgabe                 |
