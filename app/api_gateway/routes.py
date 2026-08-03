from datetime import datetime


class GatewayRoutes:


    def available_routes(self):

        return {

            "routes":

            [

                "/investigate",

                "/analyze",

                "/hunt",

                "/respond",

                "/report"

            ],

            "timestamp":

                datetime.utcnow().isoformat()

        }