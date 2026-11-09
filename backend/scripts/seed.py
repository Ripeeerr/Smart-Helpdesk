from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Priority

if __name__ == "__main__":
    with Session(engine) as session:
        if session.scalar(select(func.count()).select_from(Priority)):
            print("справочник уже заполнен")
        else:
            priorities_low, priorities_medium, priorities_high, priorities_critical = (
                Priority.create_prototypes(4)
            )
            priorities_low.name = "Низкий"
            priorities_low.sla_hours = 72

            priorities_medium.name = "Средний"
            priorities_medium.sla_hours = 24

            priorities_high.name = "Высокий"
            priorities_high.sla_hours = 8

            priorities_critical.name = "Критический"
            priorities_critical.sla_hours = 2
            session.add_all(
                [
                    priorities_low,
                    priorities_medium,
                    priorities_high,
                    priorities_critical,
                ]
            )
            session.commit()
