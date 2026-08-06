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
    Backward-compatible database helper.

    Existing services can continue using:
        Database().execute()
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

            return result.fetchall()



    def execute_one(
        self,
        query,
        params=None,
    ):

        result = self.execute(
            query,
            params,
        )

        if result:

            return result[0]

        return None