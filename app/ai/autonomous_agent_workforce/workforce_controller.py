from datetime import datetime


def generate_workforce(user_id):

    return {

        "user_id":

            user_id,


        "workforce_status":

            "active",


        "workforce_score":

            99,


        "agent_count":

            5,


        "agents":

            [

                "Planning Agent",

                "Analysis Agent",

                "Execution Agent",

                "Monitoring Agent",

                "Optimization Agent"

            ],


        "capabilities":

            [

                "Autonomous task execution",

                "Multi-agent collaboration",

                "Decision support",

                "Performance monitoring",

                "Continuous optimization"

            ],


        "generated_at":

            datetime.utcnow().isoformat(),


        "version":

            "1.0"

    }