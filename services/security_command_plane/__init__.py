from .command_center import CommandCenter
from .service_registry import ServiceRegistry
from .health_monitor import HealthMonitor
from .policy_engine import PolicyEngine
from .governance_manager import GovernanceManager
from .audit_manager import AuditManager
from .platform_controller import PlatformController
from .runtime_manager import RuntimeManager


class SecurityCommandPlane:
    """
    Sentinel DNA enterprise command and control plane.

    Coordinates:
    - service lifecycle
    - health monitoring
    - governance
    - policy enforcement
    - runtime operations
    """

    def __init__(self):
        self.command_center = CommandCenter()
        self.service_registry = ServiceRegistry()
        self.health_monitor = HealthMonitor()
        self.policy_engine = PolicyEngine()
        self.governance_manager = GovernanceManager()
        self.audit_manager = AuditManager()
        self.platform_controller = PlatformController()
        self.runtime_manager = RuntimeManager()

    def status(self):
        return {
            "component": "Security Command Plane",
            "status": "healthy"
        }