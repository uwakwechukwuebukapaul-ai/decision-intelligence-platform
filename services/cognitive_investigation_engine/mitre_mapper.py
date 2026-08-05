class MITREMapper:
    """
    MITRE ATT&CK contextual mapper.

    Initial intelligence layer.
    Later connected to ATT&CK database.
    """

    TECHNIQUE_MAP = {

        "powershell": {

            "id":
                "T1059.001",

            "name":
                "PowerShell",

            "tactic":
                "Execution"
        },

        "ransomware": {

            "id":
                "T1486",

            "name":
                "Data Encrypted for Impact",

            "tactic":
                "Impact"
        }

    }


    def map(
        self,
        case
    ):

        text = str(case).lower()

        techniques = []


        for keyword, technique in self.TECHNIQUE_MAP.items():

            if keyword in text:

                techniques.append(
                    technique
                )


        return {

            "framework":
                "MITRE ATT&CK",

            "techniques":
                techniques,

            "mapping_status":
                "completed"

        }