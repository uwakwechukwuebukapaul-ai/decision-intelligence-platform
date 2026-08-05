from .response_model import ResponseModel
from .playbook_generator import PlaybookGenerator
from .containment_engine import ContainmentEngine
from .remediation_advisor import RemediationAdvisor


class ResponseIntelligenceEngine:
    """
    Sentinel DNA Autonomous Response Intelligence Engine.

    Converts investigation results into
    response decisions.
    """

    def __init__(self):

        self.model = ResponseModel()

        self.playbooks = PlaybookGenerator()

        self.containment = ContainmentEngine()

        self.remediation = RemediationAdvisor()



    def respond(
        self,
        threat
    ):

        playbook = self.playbooks.generate(
            threat
        )


        containment = self.containment.contain(
            threat
        )


        remediation = self.remediation.advise(
            threat
        )


        return self.model.create(

            threat,

            severity=self.calculate_severity(
                threat
            ),

            actions=playbook

        ) | {


            "playbook":
                playbook,


            "containment":
                containment,


            "remediation":
                remediation

        }



    def calculate_severity(
        self,
        threat
    ):

        threat_lower = threat.lower()


        if "ransomware" in threat_lower:

            return "critical"


        if "malware" in threat_lower:

            return "high"


        return "medium"