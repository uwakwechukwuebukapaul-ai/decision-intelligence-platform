from datetime import datetime


class IncidentClassifier:


    def classify(self, incident):

        incident_lower = incident.lower()


        if "ransomware" in incident_lower:

            category = "Ransomware Attack"
            severity = "critical"


        elif "phishing" in incident_lower:

            category = "Phishing Attack"
            severity = "high"


        elif "malware" in incident_lower:

            category = "Malware Incident"
            severity = "high"


        else:

            category = "Security Incident"
            severity = "medium"



        return {

            "classification":
                category,

            "severity":
                severity,

            "incident_type":
                "Cyber Security Incident",

            "timestamp":
                datetime.utcnow().isoformat()

        }