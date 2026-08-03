from datetime import datetime


class ConversationEngine:
    """
    Handles analyst conversations.
    """

    def process(self, message):

        intent = "general_security_question"

        text = message.lower()

        if "alert" in text:
            intent = "alert_analysis"

        elif "incident" in text:
            intent = "incident_investigation"

        elif "threat" in text:
            intent = "threat_analysis"

        elif "ransomware" in text:
            intent = "malware_investigation"


        return {

            "message": message,

            "intent": intent,

            "timestamp":
                datetime.utcnow().isoformat()

        }