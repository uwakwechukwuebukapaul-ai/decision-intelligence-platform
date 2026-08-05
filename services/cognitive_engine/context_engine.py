class ContextEngine:
    """
    Builds investigation context.

    Combines:
    - assets
    - incidents
    - threats
    - historical data
    """


    def __init__(self):

        self.contexts = []



    def build(
        self,
        event,
        intelligence=None
    ):

        context = {

            "event":
                event,

            "intelligence":
                intelligence or {},

            "status":
                "context_generated"

        }


        self.contexts.append(
            context
        )


        return context



    def get_contexts(
        self
    ):

        return self.contexts