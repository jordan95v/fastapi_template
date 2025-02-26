from typing import ClassVar
from sqlalchemy.orm import QueryPropertyDescriptor
from sqlmodel import SQLModel
from core.config import SESSION

__all__: list[str] = ["Base"]


class Base(SQLModel):
    query: ClassVar[QueryPropertyDescriptor] = SESSION.query_property()
