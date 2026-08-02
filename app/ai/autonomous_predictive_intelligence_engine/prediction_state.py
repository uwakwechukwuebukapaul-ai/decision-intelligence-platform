from datetime import datetime


class PredictionState:


    def __init__(self, user_id):

        self.user_id = user_id


    def generate_state(self):

        return {

            "user_id":
                self.user_id,

            "prediction_level":
                99,

            "prediction_status":
                "active",

            "system_health":
                "optimal",

            "generated_at":
                datetime.utcnow().isoformat()

        }