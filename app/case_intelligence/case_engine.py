from datetime import datetime

from .case_repository import CaseRepository
from .case_schema import create_case



class CaseEngine:


    def __init__(self):

        self.repository = CaseRepository()



    def create_case(
        self,
        title,
        severity="medium",
        source="AI_ENGINE"
    ):

        case = create_case(
            title,
            severity,
            source
        )

        return self.repository.save(case)



    def update_status(
        self,
        case_id,
        status
    ):

        return self.repository.update(
            case_id,
            {
                "status": status,
                "updated_at": datetime.utcnow().isoformat()
            }
        )



    def assign_analyst(
        self,
        case_id,
        analyst
    ):

        return self.repository.update(
            case_id,
            {
                "assigned_to": analyst,
                "updated_at": datetime.utcnow().isoformat()
            }
        )



    def add_evidence(
        self,
        case_id,
        evidence
    ):

        case = self.repository.get(case_id)

        if not case:
            return None


        case["evidence"].append(evidence)

        case["updated_at"] = datetime.utcnow().isoformat()

        return case



    def add_note(
        self,
        case_id,
        note
    ):

        case = self.repository.get(case_id)

        if not case:
            return None


        case["notes"].append(note)

        case["updated_at"] = datetime.utcnow().isoformat()

        return case



    def close_case(
        self,
        case_id
    ):

        return self.update_status(
            case_id,
            "closed"
        )



    def get_case_summary(
        self,
        case_id
    ):

        case = self.repository.get(case_id)

        if not case:
            return None


        return {
            "case_id": case["case_id"],
            "status": case["status"],
            "severity": case["severity"],
            "assigned_to": case["assigned_to"],
            "evidence_count": len(case["evidence"]),
            "notes_count": len(case["notes"]),
            "created_at": case["created_at"]
        }