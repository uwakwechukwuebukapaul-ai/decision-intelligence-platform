from datetime import datetime


class EventNormalizer:


    def normalize(self, event):

        return {
            "original_event": event,
            "event_type": self.detect_type(event),
            "severity": self.detect_severity(event),
            "timestamp": datetime.utcnow().isoformat()
        }


    def detect_type(self, event):

        text = event.lower()

        if "ransomware" in text:
            return "malware_activity"

        if "powershell" in text:
            return "execution_activity"

        return "security_event"


    def detect_severity(self, event):

        text = event.lower()

        if "ransomware" in text:
            return "critical"

        if "malware" in text:
            return "high"

        return "medium"