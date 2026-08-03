from datetime import datetime

from app.ai.decision_memory.patterns.pattern_store import PatternStore



class PatternEngine:
    """
    Decision Pattern Intelligence

    Responsibilities:
    - Discover successful strategies
    - Calculate success rates
    - Generate recommendations
    """


    def __init__(self):

        self.store = PatternStore()



    def discover_pattern(
        self,
        domain,
        strategy,
        decisions
    ):


        total = len(decisions)


        if total == 0:

            return {

                "status":
                    "no_data"

            }



        successful = [

            item

            for item in decisions

            if item.get("outcome")
            == "success"

        ]


        success_rate = round(

            (
                len(successful)
                /
                total
            )
            *
            100,

            2

        )


        if success_rate >= 80:

            recommendation = (
                "Continue using this strategy"
            )


        elif success_rate >= 50:

            recommendation = (
                "Improve strategy execution"
            )


        else:

            recommendation = (
                "Replace strategy with alternatives"
            )



        return self.store.save_pattern(

            domain,

            strategy,

            success_rate,

            recommendation

        )



    def analyze_domain(
        self,
        domain
    ):

        return self.store.search_patterns(
            domain
        )