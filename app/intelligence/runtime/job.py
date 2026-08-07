"""
Intelligence Job

Represents a unit of intelligence execution.
"""


class IntelligenceJob:

    def __init__(
        self,
        capability,
        payload,
        context=None,
    ):

        self.capability = capability

        self.payload = payload

        self.context = context