class ResponseModel:
    """
    Normalized response decision model.
    """

    def create(
        self,
        threat,
        severity="medium",
        actions=None
    ):

        if actions is None:
            actions = []

        return {

            "threat": threat,

            "severity": severity,

            "actions": actions,

            "status":
                "response_planned"

        }