from datetime import datetime


class RuleManager:


    def __init__(self):

        self.rules = [

            {
                "name": "Suspicious Login Detection",
                "severity": "high"
            },

            {
                "name": "Malware Execution Detection",
                "severity": "critical"
            },

            {
                "name": "Privilege Escalation Detection",
                "severity": "high"
            }

        ]


    def evaluate(self,event):

        matches=[]


        text=str(event).lower()


        for rule in self.rules:

            if "login" in text or "malware" in text or "admin" in text:

                matches.append(rule)


        return {

            "matched_rules":matches,

            "count":len(matches),

            "timestamp":datetime.utcnow().isoformat()

        }