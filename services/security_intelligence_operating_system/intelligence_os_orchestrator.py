from .intelligence_os import SecurityIntelligenceOS


class IntelligenceOSOrchestrator:

    def __init__(self):

        self.engine = SecurityIntelligenceOS()


    def execute(self, intelligence):

        return self.engine.analyze(
            intelligence
        )