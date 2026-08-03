from datetime import datetime
import uuid


class CaseManager:


    def __init__(self):

        self.cases=[]



    def create_case(self, alert, severity):

        case = {

            "case_id":
                f"INC-{uuid.uuid4().hex[:8].upper()}",

            "alert": alert,

            "severity": severity["level"],

            "status": "OPEN",

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.cases.append(case)


        return case