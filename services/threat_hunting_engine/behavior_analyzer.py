class BehaviorAnalyzer:
    """
    Detects suspicious user and system behavior.
    """

    def analyze(self, events):
        findings = []

        data = str(events).lower()

        indicators = {
            "failed login": "Possible brute force activity",
            "privilege escalation": "Possible privilege escalation attempt",
            "powershell": "Possible script execution activity",
            "remote access": "Possible lateral movement activity",
            "scheduled task": "Possible persistence mechanism",
        }

        for keyword, finding in indicators.items():
            if keyword in data:
                findings.append(finding)

        return findings