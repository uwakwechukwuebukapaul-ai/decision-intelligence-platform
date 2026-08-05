class EvidenceReasoner:


    def analyze(self, evidence):

        return {
            "evidence_processed": True,
            "signals": self.extract_signals(evidence),
            "confidence": 0.75
        }


    def extract_signals(self, evidence):

        if isinstance(evidence, dict):

            return list(
                evidence.keys()
            )

        return []