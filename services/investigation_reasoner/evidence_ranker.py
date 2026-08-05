class EvidenceRanker:
    """
    Prioritizes investigation evidence.
    """

    def rank(
        self,
        evidence_items
    ):

        priority = {

            "process": "critical",

            "endpoint": "critical",

            "authentication": "high",

            "network": "high",

            "threat intelligence": "medium",

            "historical": "low"

        }


        ranked = []


        for item in evidence_items:

            level = "medium"

            for key, value in priority.items():

                if key in item.lower():

                    level = value


            ranked.append({

                "evidence": item,

                "priority": level

            })


        return ranked