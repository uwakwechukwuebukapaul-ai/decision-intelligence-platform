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


class Container:
    """
    Generic dependency registry.
    """

    def __init__(self):

        self.services = {}


    def register(
        self,
        name,
        service,
    ):

        self.services[name] = service


    def resolve(
        self,
        name,
    ):

        return self.services.get(name)


    def has(
        self,
        name,
    ):

        return name in self.services


    def clear(self):

        self.services.clear()



class ServiceContainer(Container):
    """
    Intelligence platform service container.

    Provides managed instances of core
    intelligence services.
    """


    def __init__(self):

        super().__init__()

        self._initialized = False

        self.task_manager = None
        self.policy_engine = None
        self.capability_manager = None
        self.audit_logger = None
        self.intelligence_controller = None



    def initialize(self):

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


        self.register(
            "intelligence_controller",
            self.intelligence_controller,
        )


        self._initialized = True



    def get_intelligence_controller(self):

        if not self._initialized:
            self.initialize()

        return self.intelligence_controller



    def health(self):

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



container = ServiceContainer()