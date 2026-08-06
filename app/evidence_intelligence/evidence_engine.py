from .evidence_repository import EvidenceRepository
from .evidence_schema import create_evidence


class EvidenceEngine:


    def __init__(self):

        self.repository = EvidenceRepository()



    def add_evidence(
        self,
        case_id,
        value,
        evidence_type,
        source="AI_ENGINE"
    ):

        evidence = create_evidence(
            case_id,
            value,
            evidence_type,
            source
        )

        return self.repository.save(
            evidence
        )



    def link_to_case(
        self,
        evidence,
        case_id
    ):

        evidence["case_id"] = case_id

        return evidence



    def get_case_evidence(
        self,
        case_id
    ):

        return self.repository.get_by_case(
            case_id
        )



    def classify_evidence(
        self,
        evidence_type
    ):

        return create_evidence(
            "TEMP",
            "TEMP",
            evidence_type
        )["classification"]



    def generate_evidence_summary(
        self,
        case_id
    ):

        evidence = self.get_case_evidence(
            case_id
        )

        return {

            "case_id": case_id,

            "total_evidence": len(evidence),

            "categories": list(
                set(
                    item["classification"]
                    for item in evidence
                )
            ),

            "evidence": evidence

        }