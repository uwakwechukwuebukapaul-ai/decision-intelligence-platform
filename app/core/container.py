"""
Sentinel DNA Dependency Injection Container

Central service registry responsible for:
- service lifecycle management
- dependency creation
- shared intelligence components
- future multi-tenant isolation support
"""


from app.intelligence.control_plane import (
    IntelligenceController,
    TaskManager,
    PolicyEngine,
    CapabilityManager,
    AuditLogger,
)


class ServiceContainer:
    """
    Central dependency container.

    Provides managed instances of core
    intelligence services.
    """


    def __init__(self):

        self._initialized = False

        self.task_manager = None

        self.policy_engine = None

        self.capability_manager = None

        self.audit_logger = None

        self.intelligence_controller = None



    def initialize(self):
        """
        Initialize core services.

        Designed to be called once during
        application startup.
        """

        if self._initialized:
            return


        self.task_manager = TaskManager()

        self.policy_engine = PolicyEngine()

        self.capability_manager = CapabilityManager()

        self.audit_logger = AuditLogger()


        self.intelligence_controller = IntelligenceController(
            task_manager=self.task_manager,
            policy_engine=self.policy_engine,
            capability_manager=self.capability_manager,
            audit_logger=self.audit_logger,
        )


        self._initialized = True



    def get_intelligence_controller(self):
        """
        Retrieve Intelligence Controller instance.
        """

        if not self._initialized:
            self.initialize()

        return self.intelligence_controller



    def health(self):
        """
        Container health status.
        """

        return {
            "container": "healthy"
            if self._initialized
            else "not_initialized",
            "services": {
                "task_manager": self.task_manager is not None,
                "policy_engine": self.policy_engine is not None,
                "capability_manager": self.capability_manager is not None,
                "audit_logger": self.audit_logger is not None,
                "intelligence_controller": self.intelligence_controller is not None,
            },
        }



# Global application container instance

container = ServiceContainer()