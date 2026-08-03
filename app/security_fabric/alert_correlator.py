from datetime import datetime


class AlertCorrelator:


    def correlate(self, event, entities):

        return {
            "correlated_alert": True,
            "alert_type": event["event_type"],
            "entities_found": len(
                entities["entities"]
            ),
            "confidence": "high",
            "timestamp": datetime.utcnow().isoformat()
        }