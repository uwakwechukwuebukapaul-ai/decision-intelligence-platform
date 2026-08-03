from datetime import datetime


class RuleGenerator:


    def generate(self,event):

        return {

            "rule_name":
                "AI Generated Threat Detection Rule",

            "logic":
                "Detect suspicious attacker behavior",

            "event":
                event,

            "status":
                "generated",

            "timestamp":
                datetime.utcnow().isoformat()

        }