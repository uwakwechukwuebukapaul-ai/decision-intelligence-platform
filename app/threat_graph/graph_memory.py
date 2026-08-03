from datetime import datetime


class GraphMemory:


    def __init__(self):

        self.memory = []


    def store(self, graph):

        record = {

            "graph": graph,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.memory.append(record)

        return record


    def recall(self):

        return self.memory