from datetime import datetime


class FuturePredictor:


    def predict(self, user_id, trends, probability):

        return {

            "user_id":
                user_id,

            "prediction_status":
                "completed",

            "predictions":

                [

                    {
                        "future_event":
                            "Expected positive development",

                        "probability":
                            90
                    },

                    {
                        "future_event":
                            "Potential risk scenario",

                        "probability":
                            70
                    }

                ],

            "confidence":
                99,

            "generated_at":
                datetime.utcnow().isoformat()
        }