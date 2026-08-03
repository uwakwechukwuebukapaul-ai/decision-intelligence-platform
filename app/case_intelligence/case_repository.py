from datetime import datetime
import uuid


class CaseRepository:
    """
    Stores and manages security cases.
    """

    def __init__(self):
        self.cases = []

    def create_case(self, title, severity="medium"):
        case = {
            "case_id": f"CASE-{uuid.uuid4().hex[:8].upper()}",
            "title": title,
            "severity": severity,
            "status": "OPEN",
            "created_at": datetime.utcnow().isoformat()
        }

        self.cases.append(case)

        return case

    def get_cases(self):
        return {
            "total_cases": len(self.cases),
            "cases": self.cases
        }

    def get_case(self, case_id):

        for case in self.cases:
            if case["case_id"] == case_id:
                return case

        return None