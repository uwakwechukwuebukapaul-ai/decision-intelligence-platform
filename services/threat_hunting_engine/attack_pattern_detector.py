class AttackPatternDetector:
    """
    Maps hunting findings to MITRE ATT&CK style patterns.
    """

    def detect(self, evidence):

        mappings = []

        data = str(evidence).lower()

        techniques = {
            "powershell": {
                "technique": "T1059.001",
                "name": "PowerShell",
            },
            "remote": {
                "technique": "T1021",
                "name": "Remote Services",
            },
            "credential": {
                "technique": "T1078",
                "name": "Valid Accounts",
            },
            "scheduled": {
                "technique": "T1053",
                "name": "Scheduled Task",
            },
        }

        for keyword, technique in techniques.items():

            if keyword in data:
                mappings.append(technique)

        return mappings