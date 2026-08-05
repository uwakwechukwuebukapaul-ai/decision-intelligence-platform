class InvestigationMemory:

    def __init__(self):
        self.cases = []

    def store_case(self, case):
        self.cases.append(case)
        return case

    def history(self):
        return self.cases