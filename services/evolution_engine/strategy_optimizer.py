class StrategyOptimizer:
    """
    Optimizes SOC strategies based on
    historical performance.
    """


    def __init__(self):

        self.strategies = []



    def optimize(
        self,
        strategy,
        feedback
    ):

        improved_strategy = {

            "original":
                strategy,

            "feedback":
                feedback,

            "optimized":
                True

        }


        self.strategies.append(
            improved_strategy
        )


        return improved_strategy



    def get_strategies(
        self
    ):

        return self.strategies