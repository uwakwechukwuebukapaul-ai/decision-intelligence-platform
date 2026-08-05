class CaseInterface:
    """
    Sentinel DNA case investigation interface.

    Provides:
    - case opening
    - analyst case tracking
    - case state management
    """

    def __init__(self):
        self.cases = []


    def open_case(self, case_id):

        case = {
            "case_id": case_id,
            "status": "opened",
            "investigation": "active"
        }

        self.cases.append(case)

        return case


    def update_case(self, case_id, status):

        for case in self.cases:

            if case["case_id"] == case_id:
                case["status"] = status
                return case

        return None


    def get_case(self, case_id):

        for case in self.cases:

            if case["case_id"] == case_id:
                return case

        return None


    def list_cases(self):

        return self.cases