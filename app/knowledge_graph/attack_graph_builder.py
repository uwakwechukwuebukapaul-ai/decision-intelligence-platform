from datetime import datetime


class AttackGraphBuilder:


    def build(self,event):

        return {

            "attack_chain":[

                "Initial Access",

                "Execution",

                "Persistence",

                "Impact"

            ],

            "framework":
                "MITRE ATT&CK",

            "timestamp":
                datetime.utcnow().isoformat()

        }