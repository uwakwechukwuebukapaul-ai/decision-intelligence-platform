"""
Detection rule definitions.
"""


class DetectionRule:


    def __init__(
        self,
        name,
        description,
        severity="medium"
    ):

        self.name = name

        self.description = description

        self.severity = severity



    def match(
        self,
        indicator: str
    ):

        return False