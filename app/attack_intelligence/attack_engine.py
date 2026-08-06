import uuid
from datetime import datetime

from .path_analyzer import PathAnalyzer
from .risk_propagator import RiskPropagator
from .attack_repository import AttackRepository



class AttackEngine:


    def __init__(self):

        self.analyzer = PathAnalyzer()

        self.risk = RiskPropagator()

        self.repository = AttackRepository()



    def analyze_path(
        self,
        source,
        target
    ):


        steps = self.analyzer.analyze(
            source,
            target
        )


        risk = self.risk.calculate(
            steps
        )


        result = {


            "attack_path_id":
            "PATH-" + uuid.uuid4().hex[:8].upper(),


            "source":
            source,


            "target":
            target,


            "risk_level":
            risk["risk_level"],


            "steps":
            steps,


            "blast_radius":
            risk["blast_radius"],


            "created_at":
            datetime.utcnow().isoformat()

        }


        self.repository.save(result)


        return result