class EvidenceCollector:


    def collect(self, incident):

        evidence = []


        if incident.get("indicator"):
            evidence.append({
                "type":"IOC",
                "value":incident["indicator"]
            })


        if incident.get("asset"):
            evidence.append({
                "type":"ASSET",
                "value":incident["asset"]
            })


        if incident.get("identity"):
            evidence.append({
                "type":"IDENTITY",
                "value":incident["identity"]
            })


        return evidence