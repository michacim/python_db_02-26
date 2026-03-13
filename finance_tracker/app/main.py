#Backend API mit fastapi

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud, database, reports


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():

    db = database.SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/expenses/", response_model=schemas.ExpenseResponse)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):

    return crud.create_expense(db=db, expense=expense)


@app.get("/expenses/", response_model=list[schemas.ExpenseResponse])
def read_expenses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):

    return crud.get_expenses(db, skip, limit)


@app.get("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def read_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = crud.get_expense(db, expense_id)

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@app.put("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def update_expense(
    expense_id: int,
    data: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):

    expense = crud.update_expense(db, expense_id, data)

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@app.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = crud.delete_expense(db, expense_id)

    if not expense:

        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {"message": "Expense deleted"}


@app.get(
    "/report/category/",
    response_model=list[schemas.CategorySummary]
)
def report_by_category(db: Session = Depends(get_db)):

    return reports.expenses_by_category(db)

#@app.post("/expenses/") – Neue Ausgabe hinzufügen.

#@app.get("/expenses/") – Alle Ausgaben abrufen.

#@app.get("/reports/category/") – Bericht „Gesamtausgaben pro Kategorie“.