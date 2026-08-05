class ContextBuilder:
    """
    Builds unified investigation context.
    """

    def build(
        self,
        event,
        signals,
        correlations
    ):

        return {

            "event": event,

            "signals": signals,

            "correlations": correlations,

            "context_status":
                "constructed"
        }