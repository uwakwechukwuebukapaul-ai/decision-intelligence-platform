from datetime import datetime
import uuid


class InvestmentMemory:

    def __init__(self):

        self.investments = []


    def store(self, decision):

        record = {

            "investment_id":
                "INV-" + uuid.uuid4().hex[:8].upper(),

            "decision":
                decision,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.investments.append(record)


        return {

            "status":
                "stored",

            "investment":
                record

        }



    def get_investments(self):

        return {

            "count":
                len(self.investments),

            "investments":
                self.investments

        }