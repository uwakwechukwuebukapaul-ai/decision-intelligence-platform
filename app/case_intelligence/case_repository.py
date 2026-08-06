class CaseRepository:


    def __init__(self):

        self.cases = {}



    def save(self, case):

        self.cases[case["case_id"]] = case

        return case



    def get(self, case_id):

        return self.cases.get(case_id)



    def update(self, case_id, data):

        if case_id not in self.cases:
            return None

        self.cases[case_id].update(data)

        return self.cases[case_id]