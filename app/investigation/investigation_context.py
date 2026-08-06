"""
Sentinel DNA Investigation Context

Unified investigation object.
"""


class InvestigationContext:


    def __init__(
        self,
        incident=None,
        evidence=None,
        timeline=None,
    ):

        self.incident = incident or {}

        self.evidence = evidence or []

        self.timeline = timeline or []



    def to_dict(self):

        return {

            "incident": self.incident,

            "evidence": self.evidence,

            "timeline": self.timeline,

        }