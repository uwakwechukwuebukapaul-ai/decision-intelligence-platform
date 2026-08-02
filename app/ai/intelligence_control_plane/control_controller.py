from datetime import datetime

from .intelligence_registry import IntelligenceRegistry
from .layer_monitor import LayerMonitor
from .event_bus import IntelligenceEventBus
from .capability_tracker import CapabilityTracker
from .system_state import SystemState



class ControlController:


    def __init__(self):

        self.registry = IntelligenceRegistry()

        self.monitor = LayerMonitor()

        self.event_bus = IntelligenceEventBus()

        self.capabilities = CapabilityTracker()

        self.state = SystemState()



    def generate_control_state(self, user_id):


        return {

            "user_id": user_id,


            "control_plane": {


                "control_status": "active",


                "control_score": 99,


                "generated_at":
                    datetime.utcnow().isoformat(),


                "version": "1.0"

            },


            "registry":
                self.registry.get_registry(),


            "monitor":
                self.monitor.monitor(),


            "capabilities":
                self.capabilities.analyze(),


            "system_state":
                self.state.get_state(),


            "event_bus":
                self.event_bus.get_events(),


            "overall_control_score": 99

        }