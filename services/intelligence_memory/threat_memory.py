import uuid


class ThreatMemory:


    def __init__(self, store):

        self.store = store



    def remember(
        self,
        threat_name,
        techniques=None
    ):


        threat = {

            "id":
                f"THREAT-{uuid.uuid4().hex[:8].upper()}",

            "name":
                threat_name,

            "techniques":
                techniques or []

        }


        return self.store.store_threat(threat)