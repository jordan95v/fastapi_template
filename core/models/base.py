from typing import ClassVar
from sqlalchemy.orm import QueryPropertyDescriptor
from sqlmodel import SQLModel
from core.config import SESSION

__all__: list[str] = ["Base"]


class Base(SQLModel):
    query: ClassVar[QueryPropertyDescriptor] = SESSION.query_property()

    def add(self) -> None:
        """Add an object to the session."""

        SESSION.add(self)

    def commit(self) -> None:
        """Commit the session."""

        SESSION.commit()
