class EvidenceRepository:


    def __init__(self):

        self.evidence = []



    def save(self, evidence):

        self.evidence.append(evidence)

        return evidence



    def get_by_case(self, case_id):

        return [
            item
            for item in self.evidence
            if item["case_id"] == case_id
        ]