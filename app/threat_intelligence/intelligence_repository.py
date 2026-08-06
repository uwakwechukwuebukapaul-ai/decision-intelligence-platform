"""
Sentinel DNA Intelligence Repository
"""


class IntelligenceRepository:



    def __init__(self):

        self.records = {}



    def save(
        self,
        intelligence,
    ):

        self.records[
            intelligence["ioc"]
        ] = intelligence


        return intelligence



    def get(
        self,
        ioc,
    ):

        return self.records.get(
            ioc
        )