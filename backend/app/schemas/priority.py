from pydantic import BaseModel, ConfigDict


class PriorityOut(BaseModel):
    id: int
    name: str
    sla_hours: int

    model_config = ConfigDict(from_attributes=True)
