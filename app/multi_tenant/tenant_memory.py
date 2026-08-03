from datetime import datetime
import uuid


class TenantMemory:


    def store(self, organization):

        return {

            "memory_id":
                "TEN-" + str(uuid.uuid4())[:8].upper(),

            "tenant":
                organization,

            "stored":
                [
                    "Organization profile",
                    "Subscription data",
                    "Usage history"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }