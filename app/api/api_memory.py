from datetime import datetime
import uuid



class APIMemory:


    def __init__(self):

        self.requests = []



    def store(
        self,
        request_data
    ):


        record = {


            "request_id":

                "REQ-" +
                uuid.uuid4().hex[:8].upper(),


            "request":

                request_data,


            "timestamp":

                datetime.utcnow().isoformat()

        }


        self.requests.append(record)


        return {


            "status":
                "stored",


            "record":
                record

        }



    def history(self):


        return {


            "count":
                len(self.requests),


            "requests":
                self.requests

        }