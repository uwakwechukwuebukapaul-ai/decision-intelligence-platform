"""
Sentinel DNA - Evidence Manager

Controls investigation evidence lifecycle.

Responsibilities:

- Create evidence records
- Attach evidence to incidents/cases
- Retrieve evidence
- List evidence
"""


from __future__ import annotations


from datetime import datetime

from .evidence_store import EvidenceStore





class EvidenceManager:
    """
    Investigation evidence controller.
    """



    def __init__(self):

        self.store = EvidenceStore()



    def create_evidence(
        self,
        evidence: dict,
    ) -> dict:
        """
        Register investigation evidence.
        """


        evidence["created_at"] = (
            datetime.utcnow().isoformat()
        )


        evidence["status"] = (
            "active"
        )


        return self.store.save(
            evidence
        )





    def get_evidence(
        self,
        evidence_id: str,
    ) -> dict | None:
        """
        Retrieve evidence by ID.
        """


        return self.store.get(
            evidence_id
        )





    def list_evidence(
        self,
        case_id: str | None = None,
    ) -> list:
        """
        Retrieve evidence collection.
        """


        return self.store.all(
            case_id
        )