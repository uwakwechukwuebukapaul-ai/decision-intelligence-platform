"""
Event Router

Routes intelligence events
to appropriate engines.
"""


class EventRouter:


    def __init__(self):

        self.routes = {

            "threat":
                "threat_intelligence",

            "detection":
                "detection_engine",

            "memory":
                "memory_engine",

            "response":
                "response_engine",

            "simulation":
                "threat_simulation"
        }



    def resolve(
        self,
        event_type
    ):

        return self.routes.get(
            event_type,
            "sentinel_kernel"
        )



    def route(
        self,
        event
    ):

        destination = self.resolve(
            event.get(
                "type"
            )
        )


        return {

            "destination":
                destination,

            "event":
                event,

            "routing_status":
                "completed"

        }