class CaseInterface:

    def __init__(self):
        self.cases = []


    def open_case(self, case_id):

        case = {
            "case_id": case_id,
            "status": "opened"
        }

        self.cases.append(case)

        return case


    def get_cases(self):

        return self.cases