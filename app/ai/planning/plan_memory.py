from datetime import datetime
import uuid


class PlanMemory:


    def __init__(self):

        self.plans = []



    def store(
        self,
        plan
    ):

        record = {

            "plan_id":
                "PLAN-" + str(uuid.uuid4())[:8].upper(),

            "plan":
                plan,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.plans.append(record)


        return {

            "status":
                "stored",

            "plan":
                record

        }



    def get_plans(
        self
    ):

        return {

            "count":
                len(self.plans),

            "plans":
                self.plans

        }