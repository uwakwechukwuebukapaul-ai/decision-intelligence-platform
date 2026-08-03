from datetime import datetime
import uuid


class TenantManager:
    """
    Multi-tenant foundation.
    """


    def __init__(self):

        self.tenants = []


    def create_tenant(self, name):

        tenant = {

            "tenant_id":
                "TENANT-" + str(uuid.uuid4())[:8],

            "name":
                name,

            "created_at":
                datetime.utcnow().isoformat()
        }


        self.tenants.append(tenant)

        return tenant



    def list_tenants(self):

        return {

            "tenants":
                self.tenants,

            "count":
                len(self.tenants)

        }