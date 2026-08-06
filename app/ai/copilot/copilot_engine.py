"""
Sentinel DNA AI Investigation Copilot
"""


from .copilot_schema import CopilotResponse
from .copilot_memory import CopilotMemory




class CopilotEngine:


    def __init__(self):

        self.memory = CopilotMemory()



    def assist(
        self,
        intelligence: dict,
    ) -> dict:


        indicator = intelligence.get(
            "indicator",
            "unknown"
        )


        risk = intelligence.get(
            "risk",
            {}
        )


        campaign = intelligence.get(
            "campaign",
            {}
        )


        memory = self.memory.summarize(
            intelligence
        )


        confidence = 70


        answer = (

            f"{indicator} requires investigation. "

            f"The indicator has "
            f"{risk.get('risk','unknown')} risk. "

        )


        if campaign.get(
            "campaign_detected"
        ):

            answer += (

                "Related campaign activity "
                "was detected."

            )


        recommendations = [

            "Review endpoint telemetry",

            "Search DNS logs",

            "Check related indicators",

            "Validate MITRE techniques",

        ]


        result = CopilotResponse(

            indicator=indicator,

            answer=answer,

            confidence=confidence,

            recommendations=recommendations,

        )


        response = result.to_dict()


        response["memory_context"] = memory


        return response