from datetime import datetime



class AlertTriageEngine:



    def triage(
        self,
        alert
    ):


        severity = "low"



        text = str(alert).lower()



        if (
            "attack" in text
            or
            "malware" in text
        ):

            severity = "high"



        if (
            "ransomware" in text
            or
            "breach" in text
        ):

            severity = "critical"



        return {


            "alert":
                alert,


            "priority":
                severity,


            "recommended_action":
                "Investigate immediately"
                if severity != "low"
                else "Monitor",


            "timestamp":
                datetime.utcnow().isoformat()

        }