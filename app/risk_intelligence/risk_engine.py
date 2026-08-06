from datetime import datetime

from .risk_calculator import RiskCalculator
from .risk_model import RiskModel
from .risk_repository import RiskRepository



class RiskEngine:


    def __init__(self):

        self.calculator = RiskCalculator()

        self.model = RiskModel()

        self.repository = RiskRepository()



    def evaluate(self, data):


        calculation = self.calculator.calculate(data)


        level = self.model.determine_level(
            calculation["score"]
        )


        result = {

            "risk_id":
                self.repository.generate_id(),

            "risk_score":
                calculation["score"],

            "risk_level":
                level,

            "factors":
                calculation["factors"],

            "created_at":
                datetime.utcnow().isoformat()

        }


        return self.repository.save(result)