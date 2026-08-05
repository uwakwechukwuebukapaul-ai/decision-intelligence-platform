class PlaybookEngine:
    """
    Sentinel DNA SOAR playbook library.

    Defines automated response workflows.
    """

    def __init__(self):

        self.playbooks = {

            "phishing": {

                "name": "Phishing Response",

                "actions": [
                    "extract_iocs",
                    "block_domain",
                    "notify_analyst"
                ]
            },


            "ransomware": {

                "name": "Ransomware Containment",

                "actions": [
                    "isolate_host",
                    "collect_evidence",
                    "disable_account",
                    "notify_incident_team"
                ]
            },


            "credential_compromise": {

                "name": "Credential Compromise Response",

                "actions": [
                    "disable_account",
                    "reset_password",
                    "review_login_activity"
                ]
            },


            "malware": {

                "name": "Malware Response",

                "actions": [
                    "quarantine_file",
                    "scan_endpoint",
                    "collect_artifacts"
                ]
            }

        }


    def select(
        self,
        threat_type
    ):

        return self.playbooks.get(

            threat_type.lower(),

            {
                "name": "Generic Security Response",

                "actions": [
                    "collect_evidence",
                    "notify_analyst"
                ]
            }

        )