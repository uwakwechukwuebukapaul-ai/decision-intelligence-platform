from datetime import datetime
import uuid



class AuditLogger:



    def __init__(self):

        self.logs = []



    def log(
        self,
        user_id,
        action,
        resource
    ):


        event = {


            "event_id":
                "AUDIT-" +
                uuid.uuid4().hex[:8].upper(),


            "user_id":
                user_id,


            "action":
                action,


            "resource":
                resource,


            "timestamp":
                datetime.utcnow().isoformat()

        }



        self.logs.append(
            event
        )


        return {


            "status":
                "logged",


            "event":
                event

        }



    def history(self):


        return {


            "count":
                len(self.logs),


            "events":
                self.logs

        }