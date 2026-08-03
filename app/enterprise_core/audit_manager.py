import uuid
from datetime import datetime


class AuditManager:


    def record(self, action):

        return {

            "audit_id":

                "AUDIT-"
                + uuid.uuid4().hex[:8].upper(),


            "action":

                action,


            "timestamp":

                datetime.utcnow().isoformat()
        }