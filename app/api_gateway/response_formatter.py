from datetime import datetime


class ResponseFormatter:


    def success(self, data):

        return {

            "status":

                "success",

            "gateway":

                "Sentinel DNA API Gateway",

            "response":

                data,

            "timestamp":

                datetime.utcnow().isoformat()

        }


    def error(self, message):

        return {

            "status":

                "error",

            "message":

                message,

            "timestamp":

                datetime.utcnow().isoformat()

        }