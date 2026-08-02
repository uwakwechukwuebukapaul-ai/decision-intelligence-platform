from datetime import datetime


def define_agent_roles(user_id):

    return {

        "user_id":
            user_id,


        "roles":

            {

                "Strategy Agent":
                    "Strategic planning and optimization",


                "Research Agent":
                    "Knowledge discovery and analysis",


                "Execution Agent":
                    "Task execution and workflow management",


                "Monitoring Agent":
                    "System observation and reporting",


                "Learning Agent":
                    "Continuous improvement"

            },


        "role_status":
            "optimized",


        "generated_at":
            datetime.utcnow().isoformat(),


        "version":
            "1.0"

    }