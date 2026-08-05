"""
Autonomous Orchestrator Response Coordinator Compatibility Layer

This module exists to maintain backward compatibility with older
autonomous orchestrator imports.

The canonical ResponseCoordinator implementation lives in:

services.response_engine.response_coordinator

All orchestration components should eventually migrate directly
to the central response engine.
"""


from services.response_engine.response_coordinator import ResponseCoordinator


__all__ = [
    "ResponseCoordinator"
]