from datetime import datetime
import uuid


class OrchestratorMemory:


    def __init__(self):

        self.records = []



    def store(self, data):

        record = {

            "orchestration_id":
                "ORCH-" + uuid.uuid4().hex[:8].upper(),

            "data":
                data,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.records.append(record)


        return {


            "status":
                "stored",

            "record":
                record

        }



    def get_history(self):

        return {

            "count":
                len(self.records),

            "records":
                self.records

        }