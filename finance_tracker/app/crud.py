from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas


def create_expense(db: Session, expense: schemas.ExpenseCreate):

    db_expense = models.Expense(**expense.dict())

    db.add(db_expense)

    db.commit()

    db.refresh(db_expense)

    return db_expense


def get_expenses(db: Session, skip: int = 0, limit: int = 100):

    return (
        db.query(models.Expense)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_expense(db: Session, expense_id: int):

    return (
        db.query(models.Expense)
        .filter(models.Expense.id == expense_id)
        .first()
    )


def update_expense(
    db: Session,
    expense_id: int,
    data: schemas.ExpenseCreate
):

    expense = get_expense(db, expense_id)

    if not expense:
        return None

    expense.category = data.category
    expense.amount = data.amount
    expense.date = data.date

    db.commit()

    db.refresh(expense)

    return expense


def delete_expense(db: Session, expense_id: int):

    expense = get_expense(db, expense_id)

    if not expense:
        return None

    db.delete(expense)

    db.commit()

    return expense


def get_expenses_by_category(db: Session):

    return (
        db.query(
            models.Expense.category,
            func.sum(models.Expense.amount).label("total")
        )
        .group_by(models.Expense.category)
        .all()
    )

#Erklärung
#create_expense()

#Schritte:

#1:SQLAlchemy Objekt erzeugen

#2:Objekt zur Session hinzufügen

#3:Datenbank speichern

#4:Ergebnis zurückgeben

#create_expense – Neue Ausgabe hinzufügen.

#get_expenses – Alle Ausgaben abrufen.

#get_expenses_by_category – Gesamtausgaben pro Kategorie.