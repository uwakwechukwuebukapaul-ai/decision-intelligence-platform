from datetime import datetime


class AccessPolicy:


    def evaluate(self, role):

        return {

            "role":
                role,

            "policy":
                "Enterprise SOC Access Policy",

            "decision":
                "approved",

            "timestamp":
                datetime.utcnow().isoformat()

        }