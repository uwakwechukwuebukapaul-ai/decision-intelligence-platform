from services.intelligence_fusion.intelligence_model import IntelligenceModel


class ContextBuilder:
    """
    Builds investigation context from raw security events.

    Future integrations:
    - Knowledge Graph
    - Threat Intelligence
    - Memory Engine
    - Investigation Runtime
    """

    def __init__(self):

        self.entity_patterns = {

            "powershell": "PowerShell",
            "ransomware": "Ransomware",
            "malware": "Malware",
            "phishing": "Phishing",
            "credential": "Credential Theft",
            "database": "Database",
            "server": "Server",
            "linux": "Linux",
            "windows": "Windows"

        }


    def build(
        self,
        event: str
    ) -> IntelligenceModel:

        intelligence = IntelligenceModel(
            event=event
        )

        self.extract_entities(
            event,
            intelligence
        )

        self.detect_relationships(
            intelligence
        )

        return intelligence


    def extract_entities(
        self,
        event: str,
        intelligence: IntelligenceModel
    ):

        normalized = event.lower()

        for keyword, entity in self.entity_patterns.items():

            if keyword in normalized:

                intelligence.add_entity(
                    entity
                )


    def detect_relationships(
        self,
        intelligence: IntelligenceModel
    ):

        entities = intelligence.entities


        if (
            "Ransomware" in entities
            and "PowerShell" in entities
        ):

            intelligence.add_relationship(
                "Ransomware Actor",
                "uses",
                "PowerShell"
            )


        if (
            "Ransomware" in entities
            and "Database" in entities
        ):

            intelligence.add_relationship(
                "Ransomware",
                "targets",
                "Database"
            )