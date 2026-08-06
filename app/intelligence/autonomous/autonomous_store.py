"""
Sentinel DNA - Autonomous Investigation Store
"""


from __future__ import annotations



class AutonomousStore:


    def __init__(self):

        self.records = []



    def save(
        self,
        investigation: dict,
    ):


        self.records.append(
            investigation
        )


        return investigation



    def all(self):

        return self.records