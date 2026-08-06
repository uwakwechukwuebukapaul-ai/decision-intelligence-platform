import uuid

from .correlation_schema import CorrelationResult
from .correlation_repository import CorrelationRepository



class CorrelationEngine:


    def __init__(self):

        self.repository = CorrelationRepository()



    def correlate(self, investigation):

        correlation_id = (
            f"COR-{uuid.uuid4().hex[:8]}"
        )


        entities = []

        relationships = []


        if investigation.get("indicator"):

            entities.append(
                {
                    "type": "ioc",
                    "value": investigation["indicator"]
                }
            )


        if investigation.get("incident_id"):

            relationships.append(
                {
                    "source": investigation["incident_id"],
                    "target": investigation.get("indicator"),
                    "relation": "contains_ioc"
                }
            )


        result = CorrelationResult(

            correlation_id=correlation_id,

            incident_id=investigation.get(
                "incident_id",
                "UNKNOWN"
            ),

            entities=entities,

            relationships=relationships,

            confidence=0.90
        )


        return self.repository.save(result.__dict__)