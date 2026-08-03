from datetime import datetime


class ResponseMemory:



    def __init__(self):

        self.history=[]



    def store(self,response):


        record={

            "response":response,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.history.append(record)


        return record



    def get_history(self):

        return self.history