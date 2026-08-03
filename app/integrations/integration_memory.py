from datetime import datetime
import uuid



class IntegrationMemory:



    def __init__(self):

        self.records = []



    def store(self, data):


        record = {


            "integration_id":

                "INT-" + uuid.uuid4().hex[:8].upper(),



            "data":

                data,



            "timestamp":

                datetime.utcnow().isoformat()

        }



        self.records.append(record)


        return record



    def history(self):


        return {


            "count":

                len(self.records),



            "records":

                self.records

        }