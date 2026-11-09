from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.reference import Priority
from app.db.session import get_db
from app.schemas.priority import PriorityOut

router = APIRouter(prefix="/priorities", tags=["priorities"])


@router.get("", response_model=list[PriorityOut], status_code=status.HTTP_200_OK)
def func_get_priorities(db: Annotated[Session, Depends(get_db)]) -> list[Priority]:
    return list(db.scalars(select(Priority).order_by(Priority.id)))
