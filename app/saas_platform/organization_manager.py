from datetime import datetime


class OrganizationManager:

    def create(self, organization):

        return {
            "organization": organization,
            "type": "Enterprise",
            "status": "registered",
            "created_at": datetime.utcnow().isoformat()
        }