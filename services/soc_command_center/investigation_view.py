class InvestigationView:
    """
    Investigation visibility layer.
    """


    def summarize(
        self,
        investigations=None
    ):

        investigations = investigations or []


        return {

            "status":
                "investigation_view_ready",

            "total":
                len(investigations),

            "investigations":
                investigations

        }