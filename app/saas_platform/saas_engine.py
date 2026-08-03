from datetime import datetime

from .tenant_manager import TenantManager
from .organization_manager import OrganizationManager
from .workspace_manager import WorkspaceManager
from .user_manager import UserManager
from .subscription_manager import SubscriptionManager
from .tenant_security import TenantSecurity
from .saas_memory import SaaSMemory
from .saas_logger import SaaSLogger


class SaaSEngine:

    def __init__(self):

        self.tenants = TenantManager()
        self.organizations = OrganizationManager()
        self.workspaces = WorkspaceManager()
        self.users = UserManager()
        self.subscription = SubscriptionManager()
        self.security = TenantSecurity()
        self.memory = SaaSMemory()
        self.logger = SaaSLogger()


    def onboard(self, organization):

        org = self.organizations.create(
            organization
        )

        tenant = self.tenants.create(
            organization
        )

        workspace = self.workspaces.create(
            tenant["tenant_id"]
        )

        user = self.users.create(
            f"admin@{organization.lower()}.com"
        )

        subscription = self.subscription.create(
            tenant["tenant_id"]
        )

        security = self.security.protect(
            tenant["tenant_id"]
        )

        memory = self.memory.store(
            organization
        )

        log = self.logger.log(
            "SaaS tenant onboarding completed"
        )


        return {

            "status": "completed",

            "organization": org,

            "tenant": tenant,

            "workspace": workspace,

            "user": user,

            "subscription": subscription,

            "security": security,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()
        }