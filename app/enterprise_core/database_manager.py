import sqlite3
from datetime import datetime


class DatabaseManager:


    def __init__(self):

        self.database = "sentinel.db"



    def initialize(self):

        connection = sqlite3.connect(
            self.database
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS system_events
            (
                id INTEGER PRIMARY KEY,
                event TEXT,
                created_at TEXT
            )
            """
        )


        connection.commit()

        connection.close()


        return {

            "database":
                self.database,

            "status":
                "initialized",

            "timestamp":
                datetime.utcnow().isoformat()
        }