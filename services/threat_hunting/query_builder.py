class QueryBuilder:
    """
    Builds hunting queries from attacker hypotheses.
    """


    def build(
        self,
        hypothesis
    ):

        return {

            "query":
                f"SEARCH security_events WHERE behavior='{hypothesis}'",

            "engine":
                "sentinel_hunting_query",

            "type":
                "behavior_search"

        }