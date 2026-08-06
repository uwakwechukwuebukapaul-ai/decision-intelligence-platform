from .detection_repository import DetectionRepository
from .detection_schema import create_detection


class DetectionEngine:


    def __init__(self):

        self.repository = DetectionRepository()

        self.rules = [

            {
                "name": "Suspicious Domain Detection",

                "pattern": [
                    ".xyz",
                    ".top",
                    ".click"
                ],

                "severity": "high",

                "mitre": [
                    "T1583.001 - Acquire Infrastructure: Domains"
                ]
            }

        ]



    def calculate_severity(
        self,
        indicator
    ):

        suspicious_extensions = [

            ".xyz",
            ".top",
            ".click",
            ".ru"

        ]


        for ext in suspicious_extensions:

            if ext in indicator:

                return "critical"


        return "medium"



    def evaluate_rule(
        self,
        indicator
    ):

        for rule in self.rules:

            for pattern in rule["pattern"]:

                if pattern in indicator:

                    return rule


        return None



    def map_attack(self):

        return [

            "T1583.001 - Acquire Infrastructure: Domains"

        ]



    def detect(
        self,
        indicator
    ):

        matched_rule = self.evaluate_rule(
            indicator
        )


        severity = self.calculate_severity(
            indicator
        )


        if matched_rule:

            techniques = matched_rule["mitre"]

            rule_name = matched_rule["name"]

        else:

            techniques = self.map_attack()

            rule_name = "Generic IOC Detection"



        detection = create_detection(

            indicator,

            rule_name,

            severity,

            0.90,

            techniques

        )


        return self.repository.save(
            detection
        )