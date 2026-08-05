from .service_mesh import ServiceMesh
from .dependency_registry import DependencyRegistry
from .intelligence_gateway import IntelligenceGateway
from .investigation_gateway import InvestigationGateway
from .response_gateway import ResponseGateway
from .ai_gateway import AIGateway
from .platform_orchestrator import PlatformOrchestrator
from .system_runtime import SystemRuntime


class PlatformIntegrationLayer:

    def __init__(self):

        self.registry = DependencyRegistry()
        self.mesh = ServiceMesh(self.registry)

        self.intelligence = IntelligenceGateway(
            self.mesh
        )

        self.investigation = InvestigationGateway(
            self.mesh
        )

        self.response = ResponseGateway(
            self.mesh
        )

        self.ai = AIGateway(
            self.mesh
        )

        self.orchestrator = PlatformOrchestrator(
            self
        )

        self.runtime = SystemRuntime(
            self
        )


    def health(self):

        return {
            "platform": "Sentinel DNA",
            "status": "healthy"
        }


__all__ = [
    "PlatformIntegrationLayer",
    "ServiceMesh",
    "DependencyRegistry",
    "IntelligenceGateway",
    "InvestigationGateway",
    "ResponseGateway",
    "AIGateway",
    "PlatformOrchestrator",
    "SystemRuntime",
]