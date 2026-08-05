class InvestigationCoordinator:

    def __init__(self):
        self.active_cases = []


    def start_investigation(self, case_id):

        investigation = {
            "case_id": case_id,
            "status": "investigating"
        }

        self.active_cases.append(investigation)

        return investigation


    def get_cases(self):

        return self.active_cases