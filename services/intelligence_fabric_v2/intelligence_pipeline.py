class IntelligencePipeline:
    """
    Controls intelligence processing flow.
    """

    def __init__(
        self,
        event_bus=None
    ):

        self.event_bus = event_bus


    def process(
        self,
        message
    ):

        normalized = self.normalize(
            message
        )


        if self.event_bus:

            self.event_bus.publish(
                normalized
            )


        return normalized



    def normalize(
        self,
        message
    ):

        message.severity = (
            message.severity.upper()
        )

        return message