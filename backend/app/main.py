import logging

from fastapi import FastAPI, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database import engine
from app.routers.priority_router import router as priority_router

app = FastAPI()

app.include_router(priority_router)


@app.get("/health")
def helth():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except SQLAlchemyError as exc:
        logging.getLogger("uvicorn.error").error(f"Проверка провалилась: {exc}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Невозможно подключиться к базе данных",
        )
