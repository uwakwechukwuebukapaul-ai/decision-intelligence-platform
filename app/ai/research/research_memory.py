from datetime import datetime
import uuid


class ResearchMemory:


    def __init__(self):

        self.memory = []



    def save(self, research):


        record = {


            "research_id":

                "RES-" + uuid.uuid4().hex[:8].upper(),


            "research":

                research,


            "created_at":

                datetime.utcnow().isoformat()

        }


        self.memory.append(record)


        return {


            "status":

                "stored",


            "research":

                record

        }



    def retrieve(self):


        return {


            "count":

                len(self.memory),


            "research":

                self.memory

        }