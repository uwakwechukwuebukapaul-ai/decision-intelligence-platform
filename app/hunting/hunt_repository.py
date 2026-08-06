"""
Sentinel DNA Hunt Repository

Temporary persistence layer.
"""


class HuntRepository:


    def __init__(self):

        self.hunts = []



    def save(
        self,
        hunt
    ):

        self.hunts.append(
            hunt
        )

        return hunt



    def list_all(self):

        return self.hunts