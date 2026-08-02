from datetime import datetime


def register_agents(user_id):

    return {

        "user_id":
            user_id,

        "registry_status":
            "active",

        "registered_agents":

            {

                "Strategy Agent":
                    "online",

                "Research Agent":
                    "online",

                "Execution Agent":
                    "online",

                "Monitoring Agent":
                    "online",

                "Learning Agent":
                    "online"

            },


        "agent_registry_score":
            99,


        "generated_at":
            datetime.utcnow().isoformat(),

        "version":
            "1.0"

    }