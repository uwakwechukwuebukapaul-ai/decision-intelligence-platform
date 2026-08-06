import uuid

from datetime import datetime

from .rules import match_ioc



class DetectionEngine:


    def analyze(
        self,
        indicator
    ):


        matches = match_ioc(
            indicator
        )


        detections = []


        for match in matches:

            detections.append(

                {
                    "detection_id":
                    "DET-" + uuid.uuid4().hex[:8],

                    "indicator":
                    indicator,

                    "rule":
                    match["rule"],

                    "severity":
                    match["severity"],

                    "status":
                    "new",

                    "created_at":
                    datetime.utcnow().isoformat()
                }

            )


        return detections