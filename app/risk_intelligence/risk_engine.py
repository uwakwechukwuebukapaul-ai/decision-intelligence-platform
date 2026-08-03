from datetime import datetime

from .risk_calculator import RiskCalculator
from .asset_risk import AssetRisk
from .user_risk import UserRisk
from .threat_risk import ThreatRisk
from .business_impact import BusinessImpact
from .risk_prediction import RiskPrediction
from .risk_memory import RiskMemory


class RiskIntelligenceEngine:

    def __init__(self):
        self.calculator = RiskCalculator()
        self.asset = AssetRisk()
        self.user = UserRisk()
        self.threat = ThreatRisk()
        self.business = BusinessImpact()
        self.prediction = RiskPrediction()
        self.memory = RiskMemory()

    def analyze(self, event):

        asset = self.asset.analyze(event)

        user = self.user.analyze(event)

        threat = self.threat.analyze(event)

        business = self.business.calculate(event)

        risk = self.calculator.calculate(
            threat,
            asset,
            user,
            business
        )

        prediction = self.prediction.predict(
            event,
            risk
        )

        self.memory.store(
            event,
            risk
        )

        return {
            "status": "completed",
            "event": event,
            "asset_risk": asset,
            "user_risk": user,
            "threat_risk": threat,
            "business_impact": business,
            "risk": risk,
            "prediction": prediction,
            "created_at": datetime.utcnow().isoformat()
        }