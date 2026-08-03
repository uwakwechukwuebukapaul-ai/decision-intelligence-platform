from datetime import datetime
import uuid



class MemoryAudit:


    def __init__(self):

        self.logs = []



    def record(
        self,
        user,
        action,
        resource
    ):


        event = {


            "audit_id":
                "MEM-AUDIT-" +
                uuid.uuid4().hex[:8].upper(),


            "user":
                user,


            "action":
                action,


            "resource":
                resource,


            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.logs.append(event)


        return event



    def history(self):

        return {


            "count":
                len(self.logs),


            "events":
                self.logs

        }