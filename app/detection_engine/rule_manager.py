from datetime import datetime


class RuleManager:


    def match(self, event):

        rules = []


        if "PowerShell" in event:

            rules.append(
                "Detect PowerShell Execution"
            )


        if "ransomware" in event.lower():

            rules.append(
                "Detect Ransomware Activity"
            )


        return {

            "matched_rules": rules,

            "count": len(rules),

            "timestamp": datetime.utcnow().isoformat()

        }