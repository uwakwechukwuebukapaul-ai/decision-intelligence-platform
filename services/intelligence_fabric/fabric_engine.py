from .intelligence_router import IntelligenceRouter
from .fabric_registry import FabricRegistry
from .fabric_state import FabricState
from .fabric_logger import FabricLogger


class IntelligenceFabricEngine:

    def __init__(self):

        self.router = IntelligenceRouter()
        self.registry = FabricRegistry()
        self.state = FabricState()
        self.logger = FabricLogger()


    def analyze(self, event):

        route = self.router.route(event)

        self.state.update(
            "processing"
        )

        result = {
            "event": event,
            "route": route,
            "status": "fabric_processed"
        }

        self.logger.log(
            "Intelligence fabric execution",
            result
        )

        self.state.update(
            "completed"
        )

        return result