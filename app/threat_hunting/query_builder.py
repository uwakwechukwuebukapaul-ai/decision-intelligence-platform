class QueryBuilder:


    def build_queries(
        self,
        indicator
    ):

        return [

            f"Search network connections for {indicator}",

            f"Search endpoint telemetry for {indicator}",

            f"Search authentication logs related to {indicator}",

            f"Search DNS activity for {indicator}"

        ]