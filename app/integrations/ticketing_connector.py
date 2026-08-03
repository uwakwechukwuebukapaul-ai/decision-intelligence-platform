from datetime import datetime


class TicketingConnector:



    def connect(self, system):


        return {


            "system":

                system,


            "status":

                "connected",



            "capabilities":

                [

                    "Create incidents",

                    "Update tickets",

                    "Track remediation"

                ],



            "timestamp":

                datetime.utcnow().isoformat()

        }



    def create_incident(self, title):


        return {


            "incident":

                title,


            "status":

                "created"

        }