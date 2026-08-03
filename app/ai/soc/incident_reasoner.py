from datetime import datetime



class IncidentReasoner:



    def reason(
        self,
        investigation
    ):


        findings = []



        if investigation.get(
            "risk_score",
            0
        ) > 70:


            findings.append(
                "Incident requires immediate response"
            )


        else:


            findings.append(
                "Continue monitoring activity"
            )



        return {


            "incident_summary":
                findings,


            "confidence":
                90,


            "timestamp":
                datetime.utcnow().isoformat()

        }