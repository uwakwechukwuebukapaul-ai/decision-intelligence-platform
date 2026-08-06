"""
Sentinel DNA Evidence Repository

Database persistence layer for evidence.

Responsibilities:

- Save evidence
- Retrieve evidence
- List evidence
"""


from __future__ import annotations


import json

from datetime import datetime

from app.database.db import Database





class EvidenceRepository:
    """
    Evidence database repository.
    """



    def __init__(self):

        self.db = Database()



    def save(
        self,
        evidence: dict,
    ) -> dict:
        """
        Persist evidence record.
        """


        now = (
            datetime.utcnow()
            .isoformat()
        )


        self.db.execute(

            """

            INSERT OR REPLACE INTO evidence

            (

                id,
                case_id,
                evidence_type,
                data,
                created_at

            )

            VALUES

            (

                :id,
                :case_id,
                :evidence_type,
                :data,
                :created_at

            )

            """,

            {

                "id":
                    evidence["evidence_id"],


                "case_id":
                    evidence.get(
                        "case_id"
                    ),


                "evidence_type":
                    evidence.get(
                        "type",
                        "unknown"
                    ),


                "data":
                    json.dumps(
                        evidence.get(
                            "data",
                            {}
                        )
                    ),


                "created_at":
                    evidence.get(
                        "created_at",
                        now
                    ),

            }

        )


        return evidence





    def get(
        self,
        evidence_id: str,
    ) -> dict | None:


        row = self.db.execute_one(

            """

            SELECT *

            FROM evidence

            WHERE id = :id

            """,

            {

                "id":
                    evidence_id

            }

        )


        if not row:

            return None



        return {

            "evidence_id":
                row["id"],

            "case_id":
                row["case_id"],

            "type":
                row["evidence_type"],

            "data":
                json.loads(
                    row["data"]
                ),

            "created_at":
                row["created_at"],

        }





    def list(
        self,
        case_id: str | None = None,
    ) -> list:


        if case_id:

            rows = self.db.execute(

                """

                SELECT *

                FROM evidence

                WHERE case_id = :case_id

                """,

                {

                    "case_id":
                        case_id

                }

            )

        else:

            rows = self.db.execute(

                """

                SELECT *

                FROM evidence

                """

            )



        return [

            {

                "evidence_id":
                    row["id"],

                "case_id":
                    row["case_id"],

                "type":
                    row["evidence_type"],

                "data":
                    json.loads(
                        row["data"]
                    ),

                "created_at":
                    row["created_at"],

            }

            for row in rows

        ]