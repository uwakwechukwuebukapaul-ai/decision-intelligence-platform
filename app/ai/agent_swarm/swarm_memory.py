from datetime import datetime



class SwarmMemory:


    VERSION = "1.0"



    def __init__(self):

        self.memory = []



    def store(
        self,
        agent,
        contribution
    ):


        record = {


            "agent":

                agent,


            "contribution":

                contribution,


            "timestamp":

                datetime.utcnow().isoformat()

        }


        self.memory.append(record)


        return record



    def retrieve(self):


        return {


            "swarm_memory":

                self.memory,


            "entries":

                len(self.memory),


            "status":

                "active",


            "version":

                self.VERSION

        }