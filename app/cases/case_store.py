"""
Sentinel DNA - Case Storage Layer

Temporary in-memory store.

Designed for future database replacement.
"""


class CaseStore:


    def __init__(self):

        self.cases = {}



    def save(
        self,
        case,
    ):

        self.cases[
            case.case_id
        ] = case


        return case



    def get(
        self,
        case_id: str,
    ):

        return self.cases.get(
            case_id
        )



    def all(self):

        return list(
            self.cases.values()
        )