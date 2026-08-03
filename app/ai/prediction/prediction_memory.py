from datetime import datetime
import uuid


class PredictionMemory:


    def __init__(self):

        self.predictions = []



    def store(

        self,

        prediction

    ):

        prediction_record = {

            "prediction_id":
                "PRED-" + str(uuid.uuid4())[:8].upper(),

            "prediction":
                prediction,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.predictions.append(
            prediction_record
        )


        return {

            "status":
                "stored",

            "prediction":
                prediction_record

        }



    def get_predictions(

        self

    ):

        return {

            "count":
                len(self.predictions),

            "predictions":
                self.predictions

        }



    def get_prediction(

        self,

        prediction_id

    ):


        for prediction in self.predictions:


            if prediction["prediction_id"] == prediction_id:

                return prediction



        return None



    def clear_memory(

        self

    ):

        self.predictions = []


        return {

            "status":
                "cleared"

        }