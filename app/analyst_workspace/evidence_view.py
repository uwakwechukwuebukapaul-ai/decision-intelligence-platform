"""
Evidence Presentation Layer
"""


class EvidenceView:


    def build(
        self,
        intelligence: dict,
    ) -> dict:


        return {

            "risk":
                intelligence.get(
                    "risk"
                ),

            "reputation":
                intelligence.get(
                    "reputation"
                ),

            "threat_context":
                intelligence.get(
                    "threat_context"
                ),

            "mitre_mapping":
                intelligence.get(
                    "mitre_mapping"
                ),

            "relationships":
                intelligence.get(
                    "relationships"
                ),

        }