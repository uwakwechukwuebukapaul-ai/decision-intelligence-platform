from datetime import datetime
import uuid


class StrategyMemory:
    """
    Stores strategic decisions and recommendations.
    """


    def __init__(self):

        self.strategies = []



    def save_strategy(
        self,
        mission,
        strategy,
        confidence,
        reasoning
    ):

        record = {

            "strategy_id":
                f"STRATEGY-{uuid.uuid4().hex[:8].upper()}",


            "mission":
                mission,


            "strategy":
                strategy,


            "confidence":
                confidence,


            "reasoning":
                reasoning,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.strategies.append(
            record
        )


        return {

            "status":
                "stored",

            "strategy":
                record

        }



    def get_strategies(
        self
    ):

        return {

            "count":
                len(self.strategies),


            "strategies":
                self.strategies

        }