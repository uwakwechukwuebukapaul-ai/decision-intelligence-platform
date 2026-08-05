class RemediationAdvisor:
    """
    Provides recovery and remediation guidance.
    """

    def advise(
        self,
        threat
    ):

        threat_lower = threat.lower()


        recommendations = []


        if "ransomware" in threat_lower:

            recommendations = [
                "patch vulnerable systems",
                "review backup strategy",
                "implement ransomware detection rules"
            ]


        elif "powershell" in threat_lower:

            recommendations = [
                "enable PowerShell logging",
                "apply execution restrictions",
                "review administrative privileges"
            ]


        else:

            recommendations = [
                "perform security review",
                "update monitoring rules"
            ]


        return recommendations