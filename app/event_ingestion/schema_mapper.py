from datetime import datetime


class SchemaMapper:


    def map(self, event):

        return {

            "schema":
                "Security Event Schema",

            "fields":
                [
                    "timestamp",
                    "source",
                    "event",
                    "severity",
                    "entity"
                ],

            "status":
                "mapped",

            "timestamp":
                datetime.utcnow().isoformat()

        }