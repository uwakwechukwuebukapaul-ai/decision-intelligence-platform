from datetime import datetime


class QueryBuilder:


    def generate(self, event):

        return {

            "queries": [

                "Search suspicious PowerShell execution",

                "Find abnormal process activity",

                "Identify lateral movement",

                "Detect encryption behavior"

            ],

            "generated_at":
                datetime.utcnow().isoformat()

        }