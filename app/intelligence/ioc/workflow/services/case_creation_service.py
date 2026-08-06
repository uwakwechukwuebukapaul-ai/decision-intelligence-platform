"""
Sentinel DNA

IOC Case Creation Service

Responsible for:
- Creating investigation cases
- Storing IOC evidence
- Connecting workflow intelligence
  with persistence layer
"""

from __future__ import annotations


from app.intelligence.ioc.persistence import (
    IOCCaseRepository,
    IOCEvidenceStore,
)



class CaseCreationService:
    """
    Creates persistent IOC investigation cases.
    """


    def __init__(
        self,
    ):

        self.case_repository = IOCCaseRepository()

        self.evidence_store = IOCEvidenceStore()



    def create_case(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Create investigation case from IOC intelligence.
        """


        indicator = intelligence.get(
            "indicator",
            "unknown",
        )


        evidence = {

            "risk": intelligence.get(
                "risk",
                {},
            ),

            "reputation": intelligence.get(
                "reputation",
                {},
            ),

            "threat_context": intelligence.get(
                "threat_context",
                {},
            ),

            "mitre_mapping": intelligence.get(
                "mitre_mapping",
                [],
            ),

            "relationships": intelligence.get(
                "relationships",
                [],
            ),

        }


        self.evidence_store.store(
            indicator,
            evidence,
        )


        case_data = {

            "title": "IOC Investigation",

            "severity": intelligence.get(
                "risk",
                {}
            ).get(
                "risk",
                "unknown",
            ),

            "source": "ioc-intelligence",

            "indicator": indicator,

            "evidence": evidence,

        }


        case = self.case_repository.create_case(
            case_data,
        )


        return case