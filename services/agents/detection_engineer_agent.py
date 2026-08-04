from .base_agent import BaseAgent


class DetectionEngineerAgent(BaseAgent):
    """
    Creates detection recommendations.
    """


    def __init__(self):

        super().__init__(
            "detection_engineer"
        )


    def execute(
        self,
        context
    ):

        event = context.get(
            "event",
            ""
        )


        detections = []


        if "PowerShell" in event:

            detections.append(
                "Create PowerShell execution detection rule"
            )


        if "ransomware" in event.lower():

            detections.append(
                "Create ransomware behaviour correlation rule"
            )


        return {

            "agent":
                self.name,

            "detections":
                detections,

            "timestamp":
                self.timestamp()

        }