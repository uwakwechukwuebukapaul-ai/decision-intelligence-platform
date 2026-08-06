import uuid

from .technique_mapper import TechniqueMapper
from .tactic_analyzer import TacticAnalyzer
from .mitre_repository import MitreRepository
from .mitre_schema import MitreRecord, timestamp



class MitreEngine:


    def __init__(self):

        self.mapper = TechniqueMapper()

        self.tactics = TacticAnalyzer()

        self.repository = MitreRepository()



    def analyze(self, context):


        techniques = self.mapper.map(
            context
        )


        tactics = self.tactics.analyze(
            techniques
        )


        risk_level = "critical" if (
            context.get("severity") == "critical"
        ) else "medium"



        record = MitreRecord(

            mitre_id=
            f"MITRE-{uuid.uuid4().hex[:8].upper()}",

            techniques=
            techniques,

            tactics=
            tactics,

            indicator=
            context.get("indicator"),

            risk_level=
            risk_level,

            confidence=
            0.95,

            created_at=
            timestamp()
        )


        self.repository.save(
            record.to_dict()
        )


        return record.to_dict()