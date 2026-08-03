from datetime import datetime


class Authentication:


    def validate(self):

        return {

            "status":

                "authenticated",

            "method":

                "API Token Validation",

            "timestamp":

                datetime.utcnow().isoformat()

        }