from datetime import datetime
import uuid


class EvidenceStore:


    def __init__(self):

        self.evidence = []



    def store(self, data):

        record = {


            "evidence_id":

                "EVID-" + uuid.uuid4().hex[:8].upper(),


            "data":

                data,


            "created_at":

                datetime.utcnow().isoformat()

        }


        self.evidence.append(record)


        return {


            "status":

                "stored",


            "evidence":

                record

        }



    def get_all(self):


        return {


            "count":

                len(self.evidence),


            "evidence":

                self.evidence

        }