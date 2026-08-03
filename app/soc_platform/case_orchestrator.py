from datetime import datetime
import uuid


class CaseOrchestrator:


    def __init__(self):

        self.cases = []



    def create(self, alert, analysis):


        case = {

            "case_id":
                f"SOC-{uuid.uuid4().hex[:8].upper()}",

            "alert":
                alert,

            "severity":
                analysis["severity"],

            "status":
                "OPEN",

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.cases.append(case)


        return case