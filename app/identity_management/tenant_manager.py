from datetime import datetime


class TenantManager:


    def assign_tenant(self, username):

        return {

            "tenant_id":
                "TENANT-001",

            "organization":
                "Sentinel DNA Enterprise",

            "user":
                username,

            "timestamp":
                datetime.utcnow().isoformat()

        }