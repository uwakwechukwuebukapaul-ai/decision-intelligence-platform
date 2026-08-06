"""
Sentinel DNA Evidence Store

Storage abstraction layer.

Future support:

- SQLite
- PostgreSQL
- distributed storage
"""


from __future__ import annotations





class EvidenceStore:


    def __init__(self):

        self.evidence = {}



    def save(
        self,
        evidence: dict,
    ) -> dict:


        self.evidence[
            evidence["evidence_id"]
        ] = evidence


        return evidence




    def get(
        self,
        evidence_id: str,
    ) -> dict | None:


        return self.evidence.get(
            evidence_id
        )





    def all(
        self,
        case_id: str | None = None,
    ) -> list:


        records = list(
            self.evidence.values()
        )


        if case_id:

            records = [

                item

                for item in records

                if item.get(
                    "case_id"
                ) == case_id

            ]


        return records