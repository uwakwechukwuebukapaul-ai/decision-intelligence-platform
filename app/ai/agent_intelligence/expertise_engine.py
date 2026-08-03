from datetime import datetime


class ExpertiseEngine:


    """
    Detects agent specialization
    """



    def analyze(
        self,
        profile
    ):


        domains = profile.get(
            "domains",
            []
        )


        expertise = "General Intelligence"


        if "Cybersecurity" in domains:

            expertise = "Security Intelligence"


        elif "AI SOC" in domains:

            expertise = "AI SOC Specialist"



        return {

            "agent_id":
                profile["agent_id"],


            "expertise":
                expertise,


            "domains":
                domains,


            "timestamp":
                datetime.utcnow().isoformat()

        }