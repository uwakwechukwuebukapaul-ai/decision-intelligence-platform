from datetime import datetime
import uuid


class TenantManager:

    def create(self, organization):

        return {
            "tenant_id": f"TENANT-{uuid.uuid4().hex[:8].upper()}",
            "organization": organization,
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }