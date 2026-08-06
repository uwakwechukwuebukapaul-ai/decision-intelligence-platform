from datetime import datetime


class AgentMemory:


    def __init__(self):

        self.memory = []



    def store(
        self,
        incident_id,
        agent,
        result
    ):

        record = {

            "incident_id": incident_id,

            "agent": agent,

            "result": result,

            "created_at": datetime.utcnow().isoformat()

        }


        self.memory.append(record)


        return record



    def get_history(
        self,
        incident_id
    ):

        return [

            item

            for item in self.memory

            if item["incident_id"] == incident_id

        ]