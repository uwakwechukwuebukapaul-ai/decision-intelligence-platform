from datetime import datetime

from .service_registry import ServiceRegistry
from .request_router import RequestRouter
from .authentication import Authentication
from .tenant_manager import TenantManager
from .audit_logger import AuditLogger
from .security_policy import SecurityPolicy
from .gateway_memory import GatewayMemory



class APIGateway:
    """
    Sentinel DNA Enterprise AI Gateway.

    Main communication layer between
    enterprise users and AI security engines.
    """


    def __init__(self):

        self.registry = ServiceRegistry()

        self.router = RequestRouter()

        self.auth = Authentication()

        self.tenants = TenantManager()

        self.audit = AuditLogger()

        self.policy = SecurityPolicy()

        self.memory = GatewayMemory()



    def process(self, request):


        security_check = (
            self.policy.evaluate(
                request
            )
        )


        route = (
            self.router.route(
                request
            )
        )


        audit = (
            self.audit.log(
                "Processed gateway request"
            )
        )


        result = {

            "status":
                "completed",

            "request":
                request,

            "security":
                security_check,

            "routing":
                route,

            "services":
                self.registry.get_services(),

            "audit":
                audit,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.memory.store(result)


        return result