import uuid
from datetime import datetime

from .behavior_analyzer import BehaviorAnalyzer
from .anomaly_detector import AnomalyDetector
from .risk_scoring import RiskScoring
from .ueba_repository import UEBARepository



class UEBAEngine:


    def __init__(self):

        self.behavior = BehaviorAnalyzer()

        self.detector = AnomalyDetector()

        self.scoring = RiskScoring()

        self.repository = UEBARepository()



    def analyze_behavior(
        self,
        user,
        activity
    ):


        profile = self.behavior.analyze(
            user,
            activity
        )


        anomalies = self.detector.detect(
            profile
        )


        risk = self.scoring.calculate(
            anomalies
        )


        result = {


            "event_id":
            "UEBA-" + uuid.uuid4().hex[:8].upper(),


            "user":
            user,


            "activity":
            activity,


            "risk_score":
            risk["risk_score"],


            "risk_level":
            risk["risk_level"],


            "anomalies":
            anomalies,


            "confidence":
            0.85,


            "created_at":
            datetime.utcnow().isoformat()

        }


        self.repository.save(result)


        return result