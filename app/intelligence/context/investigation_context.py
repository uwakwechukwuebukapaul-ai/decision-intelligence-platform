"""
Investigation Context

Shared intelligence state for SOC investigations.
"""


class InvestigationContext:
    """
    Represents complete investigation state.
    """

    def __init__(
        self,
        case_id,
        evidence=None,
        iocs=None,
        timeline=None,
        notes=None,
    ):

        self.case_id = case_id

        self.evidence = evidence or []

        self.iocs = iocs or []

        self.timeline = timeline or []

        self.notes = notes or []


    def summary(self):

        return {

            "case_id": self.case_id,

            "evidence_count":
                len(self.evidence),

            "ioc_count":
                len(self.iocs),

            "timeline_events":
                len(self.timeline),

            "notes_count":
                len(self.notes),

        }