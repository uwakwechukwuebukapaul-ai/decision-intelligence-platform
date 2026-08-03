from datetime import datetime
import uuid


class TenantLogger:


    def record(self, organization):

        return {

            "log_id":
                "TENLOG-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                "Tenant created",

            "organization":
                organization,

            "timestamp":
                datetime.utcnow().isoformat()

        }