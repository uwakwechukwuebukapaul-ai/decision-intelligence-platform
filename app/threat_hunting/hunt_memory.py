from datetime import datetime


class HuntMemory:


    def __init__(self):

        self.history=[]



    def store(self, hunt):


        record={

            "hunt":
                hunt,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.history.append(record)


        return record



    def get_history(self):

        return self.history