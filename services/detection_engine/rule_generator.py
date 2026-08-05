from .detection_model import DetectionModel


class RuleGenerator:
    """
    Generates detection rules from threat intelligence.
    """


    def generate(
        self,
        threat
    ):

        threat_text = threat.lower()


        rules = []

        mitre = []


        if "powershell" in threat_text:

            rules.append(
                "process=powershell.exe"
            )

            mitre.append(
                "T1059.001"
            )


        if "ransomware" in threat_text:

            rules.append(
                "behavior=file_encryption"
            )

            mitre.append(
                "T1486"
            )


        if "credential" in threat_text:

            rules.append(
                "credential_access_activity"
            )

            mitre.append(
                "T1003"
            )


        severity = "medium"


        if "ransomware" in threat_text:

            severity = "critical"


        return DetectionModel(

            name=
            "Autonomous Threat Detection Rule",


            severity=
            severity,


            description=
            "Generated from threat intelligence",


            logic=
            rules,


            mitre=
            mitre,


            metadata={

                "source":
                "sentinel_dna_ai"

            }

        ).to_dict()