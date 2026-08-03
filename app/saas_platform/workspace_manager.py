from datetime import datetime
import uuid


class WorkspaceManager:

    def create(self, tenant):

        return {
            "workspace_id": f"WORKSPACE-{uuid.uuid4().hex[:8].upper()}",
            "tenant": tenant,
            "modules": [
                "SOC Dashboard",
                "Threat Intelligence",
                "AI Investigation",
                "SOAR"
            ],
            "created_at": datetime.utcnow().isoformat()
        }