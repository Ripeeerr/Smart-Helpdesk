from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Priority(Base):
    __tablename__ = "priorities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    sla_hours: Mapped[int] = mapped_column(nullable=False)

    @classmethod
    def create_prototypes(cls, count=4):
        return tuple(cls() for _ in range(count))
