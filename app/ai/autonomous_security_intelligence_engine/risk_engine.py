from datetime import datetime


class RiskEngine:


    def __init__(self):

        self.version = "1.0"



    def evaluate(self, user_id, threats):


        detected_threats = []


        if isinstance(threats, dict):

            detected_threats = threats.get(
                "detected_threats",
                []
            )


        elif isinstance(threats, list):

            detected_threats = threats



        threat_count = len(
            detected_threats
        )



        risk_score = min(
            100,
            20 + (threat_count * 20)
        )



        if risk_score >= 80:

            level = "critical"


        elif risk_score >= 60:

            level = "high"


        elif risk_score >= 40:

            level = "medium"


        else:

            level = "low"



        return {


            "user_id":

                user_id,


            "risk_score":

                risk_score,


            "risk_level":

                level,


            "risk_status":

                "evaluated",


            "threat_count":

                threat_count,


            "threats_processed":

                detected_threats,


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }