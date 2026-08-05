from .intelligence_fabric import SentinelIntelligenceFabric


class FabricOrchestrator:


    def __init__(self):

        self.fabric = SentinelIntelligenceFabric()


    def execute(self, event):

        return self.fabric.process(
            event
        )


    def health_check(self):

        return {
            "service": "Sentinel Intelligence Fabric",
            "status": "healthy"
        }