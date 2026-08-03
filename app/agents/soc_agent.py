from datetime import datetime


class SOCAgent:


    def investigate(self, incident):

        return {

            "agent":
            "SOC Agent",

            "investigation":
            {
                "incident": incident,

                "findings":
                [
                    "Evidence collected",
                    "Threat indicators analyzed",
                    "Incident severity evaluated"
                ],

                "severity":
                "high",

                "confidence":
                90
            },

            "timestamp":
            datetime.now().isoformat()
        }