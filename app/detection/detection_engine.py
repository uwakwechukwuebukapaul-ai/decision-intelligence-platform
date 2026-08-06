"""
Sentinel DNA Detection Engine
"""


import uuid

from .detection_schema import DetectionResult
from .mitre_mapper import MitreMapper
from .detection_repository import DetectionRepository



class DetectionEngine:


    def __init__(self):

        self.mapper = MitreMapper()

        self.repository = DetectionRepository()



    def analyze(
        self,
        indicator: str
    ):


        severity = "low"

        confidence = 0.5


        if any(
            x in indicator
            for x in [
                ".xyz",
                ".top",
                ".click",
                ".ru"
            ]
        ):

            severity = "high"

            confidence = 0.90



        result = DetectionResult(

            detection_id=
                f"DET-{uuid.uuid4().hex[:8]}",

            indicator=indicator,

            rule_name=
                "Suspicious IOC Detection",

            severity=severity,

            confidence=confidence,

            mitre_techniques=
                self.mapper.map_indicator(
                    indicator
                )
        )


        return self.repository.save(
            result.__dict__
        )