"""
Sentinel DNA Evidence Store

Evidence persistence abstraction.
"""


from .evidence_repository import EvidenceRepository





class EvidenceStore:


    def __init__(self):

        self.repository = (
            EvidenceRepository()
        )



    def save(
        self,
        evidence: dict,
    ) -> dict:


        return self.repository.save(
            evidence
        )



    def get(
        self,
        evidence_id: str,
    ):


        return self.repository.get(
            evidence_id
        )



    def all(
        self,
        case_id=None,
    ):


        return self.repository.list(
            case_id
        )