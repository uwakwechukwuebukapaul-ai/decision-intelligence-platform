from datetime import datetime
import uuid


class OrganizationManager:


    def create(self, name):

        return {

            "organization_id":
                "ORG-" + str(uuid.uuid4())[:8].upper(),

            "name":
                name,

            "status":
                "active",

            "created_at":
                datetime.utcnow().isoformat()

        }