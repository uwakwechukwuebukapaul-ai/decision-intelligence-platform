"""
Fabric Controller

Controls lifecycle of
Sentinel DNA Intelligence Fabric.
"""


from .event_router import EventRouter
from .kernel_fabric_bridge import KernelFabricBridge



class FabricController:


    def __init__(
        self,
        kernel=None
    ):

        self.bridge = KernelFabricBridge(
            kernel
        )

        self.router = EventRouter()

        self.running = False



    def start(self):

        self.running = True

        return {

            "fabric":
                "started",

            "status":
                "online"

        }



    def stop(self):

        self.running = False

        return {

            "fabric":
                "stopped",

            "status":
                "offline"

        }



    def process(
        self,
        event
    ):

        route = self.router.route(
            event
        )


        self.bridge.publish_intelligence(

            source="sentinel_kernel",

            event_type=event.get(
                "type",
                "unknown"
            ),

            payload=event

        )


        return route