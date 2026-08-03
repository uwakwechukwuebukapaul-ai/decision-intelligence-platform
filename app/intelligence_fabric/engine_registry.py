class EngineRegistry:

    def __init__(self):

        self.engines = [
            "Threat Intelligence",
            "Knowledge Graph",
            "MITRE ATT&CK Intelligence",
            "Security Analytics",
            "Security Reasoning",
            "AI Copilot",
            "SOAR",
            "Incident Response"
        ]


    def list_engines(self):

        return {
            "registered_engines": self.engines,
            "count": len(self.engines)
        }