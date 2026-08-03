from datetime import datetime


class SystemMonitor:


    def __init__(self):

        self.components = {

            "AI Engine": "healthy",

            "SOC Investigation": "healthy",

            "Decision Engine": "healthy",

            "API Gateway": "healthy",

            "Memory Layer": "healthy"

        }



    def status(self):


        return {


            "system_status":

                "operational",


            "components":

                self.components,


            "timestamp":

                datetime.utcnow().isoformat()

        }