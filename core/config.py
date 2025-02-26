import os
from typing import Final
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlmodel import create_engine

__all__: list[str] = ["ENGINE", "SESSION"]

ENGINE: Final[Engine] = create_engine(os.environ["DATABASE_URI"])
SESSION: Final[scoped_session] = scoped_session(
    sessionmaker(bind=ENGINE, autocommit=False, expire_on_commit=False)
)
