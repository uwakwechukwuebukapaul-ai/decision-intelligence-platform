"""
Sentinel DNA Investigation Service

Creates complete investigation context.
"""


from .investigation_context import InvestigationContext

from .investigation_repository import (
    InvestigationRepository,
)

from app.evidence import EvidenceManager




class InvestigationService:


    def __init__(self):

        self.repository = (
            InvestigationRepository()
        )

        self.evidence = (
            EvidenceManager()
        )



    def get_investigation(
        self,
        incident_id,
    ):


        data = (
            self.repository
            .get_incident_context(
                incident_id
            )
        )


        evidence = []


        if hasattr(
            self.evidence,
            "list_by_case"
        ):

            evidence = (
                self.evidence
                .list_by_case(
                    incident_id
                )
            )


        context = InvestigationContext(

            incident=data["incident"],

            evidence=evidence,

            timeline=data["timeline"],

        )


        return context.to_dict()