"""
Sentinel DNA Database Core

Enterprise database foundation.

Provides:

- SQLAlchemy engine
- ORM Base
- Session factory
- Database helper compatibility
"""


from pathlib import Path

from sqlalchemy import (
    create_engine,
    text,
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
)





DATABASE_PATH = (
    Path(__file__)
    .resolve()
    .parent
    / "sentinel.db"
)



DATABASE_URL = (
    f"sqlite:///{DATABASE_PATH}"
)





engine = create_engine(

    DATABASE_URL,

    connect_args={
        "check_same_thread": False
    },

    future=True,

)





SessionLocal = sessionmaker(

    bind=engine,

    autoflush=False,

    autocommit=False,

    future=True,

)





Base = declarative_base()





class Database:
    """
    Backward compatible database helper.

    Supports existing services:
        Database().execute()
        Database().execute_one()
    """



    def execute(
        self,
        query,
        params=None,
    ):

        params = params or {}

        with engine.begin() as connection:

            result = connection.execute(

                text(query),

                params,

            )


            if result.returns_rows:

                return result.fetchall()


            return []





    def execute_one(
        self,
        query,
        params=None,
    ):

        params = params or {}

        with engine.begin() as connection:

            result = connection.execute(

                text(query),

                params,

            )


            if not result.returns_rows:

                return None


            row = result.fetchone()


            return row._mapping if row else None





class DatabaseSession:

    """
    SQLAlchemy session provider.
    """

    def get_session(self):

        return SessionLocal()