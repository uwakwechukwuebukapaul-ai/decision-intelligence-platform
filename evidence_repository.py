class EvidenceRepository:
    """
    Investigation evidence storage.
    """

    def __init__(self):

        self.evidence = []


    def store(self, evidence):

        item = {
            "id": len(self.evidence) + 1,
            "evidence": evidence
        }

        self.evidence.append(item)

        return item


    def list_all(self):

        return self.evidence