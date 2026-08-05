from collections import defaultdict


class EventBus:
    """
    Internal intelligence event communication bus.
    """

    def __init__(self):

        self.subscribers = defaultdict(list)


    def subscribe(
        self,
        event_type,
        callback
    ):

        self.subscribers[event_type].append(
            callback
        )


    def publish(
        self,
        message
    ):

        event_type = message.event

        responses = []


        for subscriber in self.subscribers.get(
            event_type,
            []
        ):

            responses.append(
                subscriber(message)
            )


        return responses


    def registered_events(self):

        return list(
            self.subscribers.keys()
        )