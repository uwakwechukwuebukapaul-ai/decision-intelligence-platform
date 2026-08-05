"""
Sentinel DNA Kernel Fabric Bridge

Connects Sentinel Kernel with Intelligence Fabric v2.
"""

from .kernel_fabric_bridge import KernelFabricBridge
from .event_router import EventRouter
from .fabric_controller import FabricController


__all__ = [
    "KernelFabricBridge",
    "EventRouter",
    "FabricController"
]