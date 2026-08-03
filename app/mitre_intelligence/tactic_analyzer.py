from datetime import datetime


class TacticAnalyzer:


    def analyze(self, techniques):

        tactics = []

        for item in techniques["techniques"]:
            if item["tactic"] not in tactics:
                tactics.append(
                    item["tactic"]
                )


        return {
            "tactics": tactics,
            "count": len(tactics),
            "timestamp": datetime.now().isoformat()
        }