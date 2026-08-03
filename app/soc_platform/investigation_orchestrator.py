from datetime import datetime


class InvestigationOrchestrator:


    def start(self, case):


        actions = [

            "Collect evidence",

            "Analyze indicators of compromise",

            "Map MITRE ATT&CK techniques",

            "Determine attacker behaviour",

            "Recommend containment"

        ]


        return {

            "case_id":
                case["case_id"],

            "investigation_status":
                "ACTIVE",

            "actions":
                actions,

            "timestamp":
                datetime.utcnow().isoformat()

        }