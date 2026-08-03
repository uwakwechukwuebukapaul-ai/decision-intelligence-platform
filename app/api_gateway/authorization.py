from datetime import datetime


class Authorization:


    def check(self, request_type):

        return {

            "status":

                "approved",

            "permission":

                request_type,

            "role":

                "SOC Analyst",

            "timestamp":

                datetime.utcnow().isoformat()

        }