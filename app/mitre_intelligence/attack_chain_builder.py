from datetime import datetime


class AttackChainBuilder:


    def build(self, event):

        return {

            "attack_chain":

            [

                "Initial Access",
                "Execution",
                "Persistence",
                "Defense Evasion",
                "Impact"

            ],

            "framework":

                "MITRE ATT&CK",

            "timestamp":

                datetime.utcnow().isoformat()
        }