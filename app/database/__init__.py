"""
Sentinel DNA Database Layer
"""


from .db import (
    Database,
    engine,
    Base,
)

from .repository import Repository

from .migrations import DatabaseMigration



def initialize_database():

    from .models import (
        Incident,
        Case,
        Evidence,
        TimelineEvent,
    )


    Base.metadata.create_all(
        bind=engine
    )


    DatabaseMigration().migrate()



__all__ = [

    "Database",

    "Repository",

    "engine",

    "Base",

    "initialize_database",

]