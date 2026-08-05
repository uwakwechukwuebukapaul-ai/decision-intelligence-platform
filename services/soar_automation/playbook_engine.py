class PlaybookEngine:
    """
    Manages automated SOC response playbooks.

    Examples:
    - phishing response
    - malware containment
    - account compromise response
    """

    def __init__(self):
        self.playbooks = {
            "phishing": [
                "collect_email_evidence",
                "extract_iocs",
                "block_indicators"
            ],
            "malware": [
                "isolate_endpoint",
                "collect_artifacts",
                "start_analysis"
            ]
        }

    def get_playbook(self, incident_type):

        return self.playbooks.get(
            incident_type,
            []
        )

    def register(self, name, steps):

        self.playbooks[name] = steps

        return {
            "registered": name,
            "steps": steps
        }