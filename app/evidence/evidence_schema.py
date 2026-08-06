"""
Sentinel DNA Evidence Schema

Defines evidence structure.
"""





class EvidenceSchema:


    @staticmethod
    def create(
        evidence_id: str,
        case_id: str,
        evidence_type: str,
        data: dict,
    ) -> dict:


        return {

            "evidence_id":
                evidence_id,

            "case_id":
                case_id,

            "type":
                evidence_type,

            "data":
                data,

        }