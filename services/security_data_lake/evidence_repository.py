class EvidenceRepository:
    """
    Investigation evidence storage layer.

    Stores:
    - files
    - logs
    - screenshots
    - forensic artifacts
    - analyst collected evidence
    """

    def __init__(self):

        self.evidence = []


    def store(self, evidence):

        record = {
            "id": len(self.evidence) + 1,
            "evidence": evidence
        }

        self.evidence.append(record)

        return record


    def get_evidence(self):

        return self.evidence


    def find(self, keyword):

        results = []

        for item in self.evidence:

            if keyword.lower() in str(item).lower():

                results.append(item)

        return results


    def count(self):

        return len(self.evidence)