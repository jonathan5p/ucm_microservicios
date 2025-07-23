from contextlib import contextmanager
from datetime import datetime
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from almacen.config import app_config
from almacen.db.tables import BaseEntity


class PostgresDB:
    def __init__(self) -> None:
        self._engine = self._create_engine()
        self._start_time = datetime.utcnow()
        self._engine.connect()
        self.initialize_tables()

    @staticmethod
    def _create_engine():
        return create_engine(
            app_config.SQLALCHEMY_DATABASE_URI,
        )

    def initialize_tables(self) -> None:
        BaseEntity.metadata.create_all(self._engine)

    @contextmanager
    def get_session(self) -> Iterator[Session]:
        with Session(self._engine) as session:
            yield session


db = PostgresDB()
