"""
Kernel Fabric Bridge

Provides communication between:

Sentinel Kernel
        |
        |
Intelligence Fabric v2
"""


from services.intelligence_fabric_v2 import (
    EventBus,
    EngineMessage
)


class KernelFabricBridge:

    def __init__(self, kernel=None):

        self.kernel = kernel

        self.event_bus = EventBus()

        self.status = "initialized"


    def publish_intelligence(
        self,
        source,
        event_type,
        payload
    ):

        message = EngineMessage(
            source=source,
            event_type=event_type,
            payload=payload
        )

        return self.event_bus.publish(
            message
        )


    def receive_event(
        self,
        message
    ):

        if self.kernel:

            return self.kernel.process(
                message
            )


        return {
            "status": "received",
            "message": message
        }


    def health(self):

        return {
            "bridge": "online",
            "status": self.status
        }