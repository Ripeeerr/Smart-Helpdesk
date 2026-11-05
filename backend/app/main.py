import logging

from app.database import engine
from fastapi import FastAPI, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()


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
