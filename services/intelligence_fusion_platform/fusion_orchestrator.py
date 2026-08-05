from .ioc_intelligence import IOCIntelligence
from .mitre_context import MITREContext
from .threat_context_builder import ThreatContextBuilder
from .risk_reasoner import RiskReasoner
from .attack_story_builder import AttackStoryBuilder



class FusionOrchestrator:
    """
    Central intelligence fusion controller.
    """


    def __init__(self):

        self.ioc = IOCIntelligence()

        self.mitre = MITREContext()

        self.context_builder = ThreatContextBuilder()

        self.risk = RiskReasoner()

        self.story = AttackStoryBuilder()



    def analyze(
        self,
        event,
        indicators=None
    ):

        if indicators is None:
            indicators = []


        ioc_data = self.ioc.analyze(
            indicators
        )


        mitre_data = self.mitre.map(
            event
        )


        context = self.context_builder.build(
            event,
            {
                "source":
                "Sentinel DNA"
            },
            mitre_data,
            ioc_data
        )


        risk = self.risk.calculate(
            context
        )


        story = self.story.build(
            context,
            risk
        )


        return {

            "context":
                context,

            "risk":
                risk,

            "attack_story":
                story

        }