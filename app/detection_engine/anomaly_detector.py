from datetime import datetime


class AnomalyDetector:


    def detect(self,event):

        text=str(event).lower()


        anomaly=False


        reasons=[]


        if "unusual" in text:

            anomaly=True
            reasons.append(
                "Unusual activity detected"
            )


        if "multiple login" in text:

            anomaly=True
            reasons.append(
                "Multiple authentication attempts"
            )


        return {

            "anomaly":anomaly,

            "reasons":reasons,

            "timestamp":datetime.utcnow().isoformat()

        }