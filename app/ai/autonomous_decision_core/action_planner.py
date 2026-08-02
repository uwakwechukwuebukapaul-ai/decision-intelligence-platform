from datetime import datetime


def create_action_plan(user_id):

    return {

        "user_id": user_id,

        "plan_status":
            "ready",

        "actions":

            [

                "Validate decision",

                "Create execution workflow",

                "Monitor outcome",

                "Capture feedback"

            ],

        "planning_score":
            99,

        "generated_at":
            datetime.utcnow().isoformat(),

        "version":
            "1.0"

    }