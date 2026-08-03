from datetime import datetime


class DetectionMemory:


    def __init__(self):

        self.history=[]


    def store(self,data):

        record={

            "data":data,

            "timestamp":datetime.utcnow().isoformat()

        }


        self.history.append(record)


        return record


    def get_history(self):

        return self.history