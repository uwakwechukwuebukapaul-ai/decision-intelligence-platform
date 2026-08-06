"""
Sentinel DNA Memory Storage Layer
"""


class MemoryStore:


    def __init__(self):

        self.records = []



    def save(
        self,
        record,
    ):

        self.records.append(
            record
        )

        return record



    def all(self):

        return self.records



    def find(
        self,
        indicator,
    ):

        return [

            record

            for record in self.records

            if record.indicator == indicator

        ]