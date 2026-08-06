class PlaybookManager:


    def __init__(self):

        self.playbooks = {

            "malware_response": [

                "block_indicator",

                "collect_telemetry",

                "notify_security_team"

            ],


            "identity_compromise": [

                "disable_account",

                "reset_credentials",

                "notify_security_team"

            ]

        }



    def get_playbook(
        self,
        name
    ):

        return self.playbooks.get(
            name,
            []
        )



    def select_playbook(
        self,
        incident
    ):

        severity = incident.get(
            "severity",
            ""
        ).lower()


        if severity == "critical":

            return "malware_response"


        return "identity_compromise"