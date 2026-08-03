from datetime import datetime
import uuid


class DashboardMemory:


    def __init__(self):

        self.history = []



    def store(self, decision):


        record = {

            "dashboard_id":
                "DASH-" + uuid.uuid4().hex[:8].upper(),

            "decision":
                decision,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.history.append(record)


        return {


            "status":
                "stored",

            "record":
                record

        }



    def get_history(self):

        return {

            "count":
                len(self.history),

            "decisions":
                self.history

        }