from typing import Dict, List


class PlaybookManager:
    """
    Manages autonomous SOC response playbooks.

    Maps security scenarios to
    predefined investigation and
    response workflows.
    """


    def __init__(self):

        self.playbooks = {

            "ransomware": {

                "name":
                    "ransomware_containment",

                "actions": [

                    "isolate affected hosts",

                    "collect forensic evidence",

                    "disable compromised accounts",

                    "start recovery workflow"

                ]

            },


            "phishing": {

                "name":
                    "phishing_investigation",

                "actions": [

                    "extract indicators",

                    "analyze email artifacts",

                    "block malicious domains",

                    "notify affected users"

                ]

            },


            "credential_theft": {

                "name":
                    "credential_compromise_response",

                "actions": [

                    "force password reset",

                    "revoke active sessions",

                    "review authentication logs"

                ]

            },


            "default": {

                "name":
                    "general_security_investigation",

                "actions": [

                    "collect telemetry",

                    "analyze indicators",

                    "monitor activity"

                ]

            }

        }



    def select_playbook(
        self,
        threat_type: str
    ):

        threat_type = (
            threat_type.lower()
            if threat_type
            else "default"
        )


        return self.playbooks.get(

            threat_type,

            self.playbooks["default"]

        )



    def list_playbooks(self) -> List[str]:

        return list(
            self.playbooks.keys()
        )



    def register_playbook(
        self,
        name: str,
        actions: List[str]
    ):

        self.playbooks[name] = {

            "name":
                name,

            "actions":
                actions

        }


        return self.playbooks[name]