import uuid
from datetime import datetime


class DashboardMemory:


    def store(self, dashboard_data):

        return {

            "memory_id":
                "DASH-"
                + uuid.uuid4().hex[:8].upper(),

            "stored":

            [
                "Dashboard state",
                "SOC metrics",
                "Analyst views"
            ],

            "dashboard_data":
                dashboard_data,

            "timestamp":
                datetime.utcnow().isoformat()
        }