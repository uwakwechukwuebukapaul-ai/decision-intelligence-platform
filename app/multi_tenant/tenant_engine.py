from datetime import datetime

from .organization_manager import OrganizationManager
from .tenant_isolation import TenantIsolation
from .subscription_manager import SubscriptionManager
from .quota_manager import QuotaManager
from .data_partition import DataPartition
from .tenant_memory import TenantMemory
from .tenant_logger import TenantLogger


class MultiTenantEngine:

    def __init__(self):

        self.organizations = OrganizationManager()
        self.isolation = TenantIsolation()
        self.subscription = SubscriptionManager()
        self.quota = QuotaManager()
        self.partition = DataPartition()
        self.memory = TenantMemory()
        self.logger = TenantLogger()


    def create_tenant(self, organization_name):

        organization = self.organizations.create(
            organization_name
        )

        isolation = self.isolation.configure(
            organization_name
        )

        subscription = self.subscription.assign(
            organization_name
        )

        quota = self.quota.allocate(
            subscription["plan"]
        )

        partition = self.partition.create(
            organization_name
        )

        memory = self.memory.store(
            organization_name
        )

        log = self.logger.record(
            organization_name
        )


        return {

            "status": "completed",

            "organization": organization,

            "isolation": isolation,

            "subscription": subscription,

            "quota": quota,

            "data_partition": partition,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.utcnow().isoformat()
        }