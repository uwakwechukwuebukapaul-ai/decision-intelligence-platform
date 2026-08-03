from datetime import datetime


class CopilotInterface:


    def assist(self, incident):

        return {

            "assistant":

                "Sentinel DNA SOC Copilot",

            "analysis":

                "AI generated investigation guidance",

            "suggestions":

            [

                "Review indicators",

                "Check affected assets",

                "Run threat hunt",

                "Execute response plan"

            ],

            "timestamp":

                datetime.utcnow().isoformat()

        }