class AttackStoryBuilder:
    """
    Converts technical evidence into analyst narrative.
    """


    def build(
        self,
        context,
        risk
    ):

        return {

            "summary":
                self.generate_summary(
                    context
                ),

            "risk":
                risk,

            "attack_chain":

                [
                    "Initial Access",
                    "Execution",
                    "Impact"
                ]
        }



    def generate_summary(
        self,
        context
    ):

        return (
            "Potential threat activity detected involving "
            + context.get(
                "event",
                "unknown activity"
            )
        )