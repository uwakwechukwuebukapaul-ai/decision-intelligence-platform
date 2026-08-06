"""
Sentinel DNA - Correlation Store

Temporary memory-backed correlation storage.

Future:

- PostgreSQL
- Elasticsearch
- Graph database
"""


class CorrelationStore:



    def __init__(self):

        self.records = []





    def save(
        self,
        record: dict,
    ):

        self.records.append(
            record
        )





    def search(
        self,
        indicator: str,
    ):

        results = []


        for record in self.records:


            if record.get(
                "indicator"
            ) == indicator:


                results.append(
                    {
                        "type": "historical_match",
                        "record": record,
                    }
                )


        return results