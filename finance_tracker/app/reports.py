# Analysen und Reports

from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Expense


def expenses_by_category(db: Session):

    result = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total")
        )
        .group_by(Expense.category)
        .all()
    )

    return result