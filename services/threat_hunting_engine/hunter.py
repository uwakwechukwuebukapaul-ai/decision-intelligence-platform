from .hunt_orchestrator import HuntOrchestrator


class ThreatHunter:
    """
    Autonomous threat hunting entry point.

    Coordinates:
    - hypothesis generation
    - IOC hunting
    - behavior analysis
    - attack pattern detection
    """

    def __init__(self):
        self.orchestrator = HuntOrchestrator()

    def execute_hunt(self, hunt_request):
        return self.orchestrator.run(hunt_request)

    def hunt(self, data):
        return self.execute_hunt(data)