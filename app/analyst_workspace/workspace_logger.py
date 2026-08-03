from datetime import datetime


class WorkspaceLogger:


    def record(self, incident):

        return {

            "event":

                "SOC workspace opened",

            "incident":

                incident,

            "timestamp":

                datetime.utcnow().isoformat()

        }