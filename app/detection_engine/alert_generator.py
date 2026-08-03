from datetime import datetime
import uuid


class AlertGenerator:


    def generate(self, event, rule):

        return {

            "alert_id":
                "ALERT-" +
                str(uuid.uuid4())[:8].upper(),

            "title":
                "Sentinel DNA Detection Alert",

            "severity":
                rule["severity"],

            "priority":
                "P1"
                if rule["severity"] == "critical"
                else "P3",

            "event":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }