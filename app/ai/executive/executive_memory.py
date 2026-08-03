from datetime import datetime
import uuid



class ExecutiveMemory:


    def __init__(self):

        self.records = []



    def store(
        self,
        data
    ):


        record = {

            "executive_id":
                "EXEC-"
                +
                uuid.uuid4().hex[:8].upper(),


            "data":
                data,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.records.append(
            record
        )


        return {

            "status":
                "stored",


            "executive_record":
                record

        }



    def get_records(
        self
    ):


        return {

            "count":
                len(self.records),


            "records":
                self.records

        }