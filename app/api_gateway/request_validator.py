from datetime import datetime


class RequestValidator:


    def validate(self, payload):

        valid = isinstance(
            payload,
            dict
        )


        return {

            "status":

                "passed" if valid else "failed",

            "checked_fields":

                list(payload.keys())
                if valid else [],

            "timestamp":

                datetime.utcnow().isoformat()

        }