from datetime import datetime


class SOCMemory:


    def __init__(self):

        self.events = []



    def store(self, event):


        record = {

            "event":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.events.append(record)


        return record



    def history(self):

        return self.events