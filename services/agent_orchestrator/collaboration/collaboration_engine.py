class CollaborationEngine:
    """
    Coordinates autonomous SOC agent collaboration.
    """


    def __init__(
        self,
        registry=None
    ):

        self.registry = registry

        self.history = []



    def send_message(
        self,
        message
    ):

        self.history.append(
            message.to_dict()
        )


        receiver = (

            self.registry.get(
                message.receiver
            )

            if self.registry
            else None

        )


        if receiver:

            result = receiver.execute(
                message.payload
            )


            return {

                "status": "delivered",

                "agent": message.receiver,

                "response": result

            }


        return {

            "status": "queued",

            "agent": message.receiver

        }



    def get_history(self):

        return self.history