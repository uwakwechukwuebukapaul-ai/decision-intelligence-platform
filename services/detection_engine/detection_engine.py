from .rule_generator import RuleGenerator
from .rule_validator import RuleValidator
from .correlation_engine import CorrelationEngine


class DetectionEngine:
    """
    Sentinel DNA Autonomous Detection Engineering Engine.

    Responsibilities:

    - Generate detection rules
    - Validate detection logic
    - Analyze security events
    - Map events to detection patterns
    - Generate Sigma compatible detections
    - Correlate security events
    """


    def __init__(self):

        self.generator = RuleGenerator()

        self.validator = RuleValidator()

        self.correlation = CorrelationEngine()



    def detect(
        self,
        threat
    ):
        """
        Autonomous detection generation pipeline.
        """


        rule = self.generator.generate(
            threat
        )


        validation = self.validator.validate(
            rule
        )


        return {

            "rule":
                rule,


            "validation":
                validation,


            "status":
                "detection_generated"

        }



    def analyze(
        self,
        event
    ):
        """
        Backward compatible detection analysis API.

        Returns:

        - patterns
        - generated rules
        - Sigma rules
        - validation results
        """


        detection = self.detect(
            event
        )


        patterns = []


        event_lower = event.lower()



        pattern_map = {


            "powershell":
                "PowerShell execution",


            "ransomware":
                "Ransomware activity",


            "malware":
                "Malware execution",


            "credential":
                "Credential access attempt",


            "phishing":
                "Phishing attempt",


            "exploit":
                "Exploit activity",


            "database":
                "Database targeting",


            "attack":
                "Unauthorized attack activity"

        }



        for keyword, pattern in pattern_map.items():

            if keyword in event_lower:

                patterns.append(
                    pattern
                )



        sigma_rule = {


            "framework":
                "Sigma",


            "title":
                "Sentinel DNA Autonomous Detection Rule",


            "description":
                event,


            "logsource":
                {

                    "product":
                        "security",

                    "service":
                        "sentinel-dna"

                },


            "detection":
                {

                    "keywords":
                        patterns

                },


            "level":
                "high" if patterns else "low",


            "status":
                "validated"

        }



        return {


            "event":
                event,


            "patterns":
                patterns,


            "rules":
                [

                    detection["rule"]

                ],


            "sigma":
                [

                    sigma_rule

                ],


            "validation":
                detection["validation"],


            "detection":
                detection,


            "status":
                "detection_processed"

        }



    def correlate(
        self,
        events
    ):
        """
        Detection correlation engine.

        Future:

        - attack chain correlation
        - MITRE ATT&CK mapping
        - behavioural analytics
        """


        return self.correlation.correlate(
            events
        )