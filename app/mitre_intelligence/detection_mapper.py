from datetime import datetime


class DetectionMapper:


    def map(self, techniques):

        detections = []


        for technique in techniques["techniques"]:

            detections.append(

                {

                    "technique":
                        technique["id"],

                    "detection_rule":
                        f"Detect {technique['name']} activity",

                    "status":
                        "enabled"

                }

            )


        return {

            "detections":
                detections,

            "timestamp":
                datetime.utcnow().isoformat()
        }