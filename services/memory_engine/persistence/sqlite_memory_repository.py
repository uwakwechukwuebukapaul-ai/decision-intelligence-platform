import sqlite3
import json
from datetime import datetime, timezone
from pathlib import Path


class SQLiteMemoryRepository:
    """
    Sentinel DNA SQLite Memory Repository.

    Provides persistent storage for:

    - Investigation memories
    - Incident knowledge
    - Threat patterns
    - Security intelligence

    Designed as a replacement backend
    for MemoryStore without changing
    higher-level intelligence services.
    """


    def __init__(
        self,
        database_path="data/sentinel_memory.db"
    ):

        self.database_path = Path(
            database_path
        )


        self.database_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        self._initialize()



    def _connection(self):

        return sqlite3.connect(
            self.database_path
        )



    def _initialize(self):

        with self._connection() as connection:

            cursor = connection.cursor()


            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    memory_type TEXT NOT NULL,

                    data TEXT NOT NULL,

                    created_at TEXT NOT NULL

                )
                """
            )


            connection.commit()



    def store(
        self,
        memory_type,
        data
    ):

        record = {

            "type":
                memory_type,

            "data":
                data

        }


        with self._connection() as connection:

            cursor = connection.cursor()


            cursor.execute(
                """
                INSERT INTO memories
                (
                    memory_type,
                    data,
                    created_at
                )
                VALUES
                (?, ?, ?)
                """,
                (

                    memory_type,

                    json.dumps(
                        data
                    ),

                    datetime.now(
                        timezone.utc
                    ).isoformat()

                )
            )


            connection.commit()


            record["id"] = cursor.lastrowid


        return record



    def get_all(
        self
    ):

        with self._connection() as connection:

            cursor = connection.cursor()


            cursor.execute(
                """
                SELECT
                    id,
                    memory_type,
                    data,
                    created_at
                FROM memories
                ORDER BY id DESC
                """
            )


            rows = cursor.fetchall()


        results = []


        for row in rows:

            results.append(

                {

                    "id":
                        row[0],

                    "type":
                        row[1],

                    "data":
                        json.loads(
                            row[2]
                        ),

                    "created_at":
                        row[3]

                }

            )


        return results



    def search(
        self,
        keyword
    ):

        keyword = keyword.lower()


        memories = self.get_all()


        results = []


        for memory in memories:

            content = str(
                memory
            ).lower()


            if keyword in content:

                results.append(
                    memory
                )


        return results