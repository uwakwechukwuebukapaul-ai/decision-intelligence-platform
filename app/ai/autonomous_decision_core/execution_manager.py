from datetime import datetime


def manage_execution(user_id):

    return {

        "user_id": user_id,

        "execution_status":
            "active",

        "execution_score":
            99,

        "workflow":

            [

                "Initialize execution",

                "Apply decision actions",

                "Monitor progress",

                "Complete objective"

            ],

        "generated_at":
            datetime.utcnow().isoformat(),

        "version":
            "1.0"

    }