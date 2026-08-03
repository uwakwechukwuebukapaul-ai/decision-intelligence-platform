from datetime import datetime


class EvidenceFusion:


    def fuse(self, event, entities, alerts):

        return {
            "evidence_sources": [
                "Detection Intelligence",
                "Threat Hunting",
                "AI Investigation",
                "Knowledge Graph"
            ],
            "entities": entities["entities"],
            "alert_confidence": alerts["confidence"],
            "timestamp": datetime.utcnow().isoformat()
        }