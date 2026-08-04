class FabricRegistry:


    def __init__(self):

        self.components = {

            "intelligence_core": "active",

            "intelligence_fusion": "active",

            "investigation_runtime": "active",

            "autonomous_orchestrator": "active"

        }


    def get_components(self):

        return self.components