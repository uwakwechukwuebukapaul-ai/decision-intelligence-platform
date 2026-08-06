"""
Detection persistence layer.
"""


class DetectionRepository:


    def __init__(self):

        self.storage = []



    def save(
        self,
        detection
    ):

        self.storage.append(
            detection
        )

        return detection



    def list_all(self):

        return self.storage