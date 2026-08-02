from datetime import datetime



class KnowledgePool:


    VERSION = "1.0"



    def __init__(self):

        self.knowledge = []



    def add_intelligence(
            self,
            agent,
            insight
    ):

        entry = {

            "agent": agent,

            "insight": insight,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.knowledge.append(entry)


        return entry



    def get_shared_knowledge(self):

        return {


            "knowledge_pool":

                self.knowledge,


            "total_entries":

                len(self.knowledge),


            "pool_status":

                "active",


            "version":

                self.VERSION


        }