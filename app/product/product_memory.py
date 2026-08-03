from datetime import datetime
import uuid



class ProductMemory:



    def __init__(self):

        self.records = []



    def store(
        self,
        data
    ):


        record = {


            "product_memory_id":

                "PROD-" + uuid.uuid4().hex[:8].upper(),



            "data":

                data,



            "created_at":

                datetime.utcnow().isoformat()


        }



        self.records.append(
            record
        )



        return record



    def history(self):


        return {


            "count":

                len(self.records),


            "records":

                self.records

        }