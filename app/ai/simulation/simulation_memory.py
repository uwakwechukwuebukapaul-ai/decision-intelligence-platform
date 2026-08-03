from datetime import datetime
import uuid


class SimulationMemory:


    def __init__(self):

        self.records = []



    def store(
        self,
        simulation
    ):

        record = {

            "simulation_id":
                "SIM-" + uuid.uuid4().hex[:8].upper(),

            "simulation":
                simulation,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.records.append(record)


        return record



    def history(self):

        return {

            "count":
                len(self.records),

            "simulations":
                self.records

        }