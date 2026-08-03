from datetime import datetime


class PlaybookManager:
    """
    Manages automated security playbooks.
    """


    def get_playbook(
        self,
        incident
    ):


        playbook = "standard_security_response"


        if "ransomware" in incident.lower():

            playbook = "ransomware_containment_playbook"



        return {

            "incident":
                incident,

            "playbook":
                playbook,

            "steps":
                [

                    "Analyze incident",

                    "Collect evidence",

                    "Contain threat",

                    "Execute remediation"

                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }