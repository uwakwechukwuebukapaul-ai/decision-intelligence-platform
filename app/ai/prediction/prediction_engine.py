from datetime import datetime

from .probability_model import ProbabilityModel
from .trend_analyzer import TrendAnalyzer
from .prediction_memory import PredictionMemory



class PredictionEngine:


    def __init__(self):

        self.probability = ProbabilityModel()

        self.trend = TrendAnalyzer()

        self.memory = PredictionMemory()



    def predict(

        self,

        mission,

        knowledge,

        simulations

    ):


        trends = self.trend.analyze(
            knowledge
        )


        probability = self.probability.calculate(
            trends["trends"]
        )


        prediction = {

            "mission":
                mission,


            "forecast":
                self.generate_forecast(
                    mission,
                    trends
                ),


            "drivers":
                trends["trends"],


            "simulation_inputs":
                simulations,


            "probability":
                probability["probability"],


            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            prediction
        )


        return {

            "status":
                "completed",

            "prediction":
                prediction

        }



    def generate_forecast(
        self,
        mission,
        trends
    ):

        if "AI" in mission:

            return (
                "AI adoption and market opportunity "
                "are expected to continue increasing"
            )


        return (
            "Future outcome requires additional intelligence"
        )