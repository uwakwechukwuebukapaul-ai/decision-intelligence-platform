from datetime import datetime


class QueryAssistant:

    def generate(self, question):

        return {
            "generated_queries": [
                "Search related security events",
                "Find affected assets",
                "Review attacker behavior"
            ],
            "question": question,
            "timestamp": datetime.utcnow().isoformat()
        }