from datetime import datetime
import uuid


class PatternStore:
    """
    Persistent Pattern Storage Layer

    Stores:
    - discovered patterns
    - success rates
    - recommendations
    """


    def __init__(self):

        self.patterns = []



    def save_pattern(
        self,
        domain,
        strategy,
        success_rate,
        recommendation
    ):

        pattern = {

            "pattern_id":
                f"PATTERN-{uuid.uuid4().hex[:8].upper()}",


            "domain":
                domain,


            "strategy":
                strategy,


            "success_rate":
                success_rate,


            "recommendation":
                recommendation,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.patterns.append(
            pattern
        )


        return {

            "status":
                "stored",


            "pattern":
                pattern

        }



    def get_patterns(
        self
    ):

        return {

            "count":
                len(self.patterns),


            "patterns":
                self.patterns

        }



    def search_patterns(
        self,
        domain
    ):


        results = [

            pattern

            for pattern in self.patterns

            if domain.lower()
            in pattern["domain"].lower()

        ]


        return {

            "count":
                len(results),


            "patterns":
                results

        }