#Aufgabe: Validierung mit Pydantic
#FastAPI nutzt Pydantic für Validierung.

from pydantic import BaseModel, Field
from datetime import date


class ExpenseBase(BaseModel):

    category: str

    amount: float = Field(gt=0)

    date: date


class ExpenseCreate(ExpenseBase):

    pass


class ExpenseResponse(ExpenseBase):

    id: int

    class Config:

        orm_mode = True          #orm_mode = True → erlaubt SQLAlchemy Objekt → Pydantic Conversion


class CategorySummary(BaseModel):

    category: str

    total: float         
        

#| Klasse        | Funktion               |
#| ------------- | ---------------------- |
#| ExpenseBase   | gemeinsame Felder      |
#| ExpenseCreate | Schema zum Erstellen   |
#| Expense       | Schema zum Zurückgeben |
#  ExpenseResponse Rückgabe an API-Client, inkl. id