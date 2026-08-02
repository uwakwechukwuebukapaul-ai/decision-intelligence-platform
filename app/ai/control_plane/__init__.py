"""
Autonomous Intelligence Control Plane v47

Central coordination layer for:
- engine registration
- intelligence routing
- execution monitoring
- autonomous workflow control
"""


from app.ai.control_plane.controller import (
    ControlPlane
)


from app.ai.control_plane.engine_registry import (
    EngineRegistry
)


from app.ai.control_plane.execution_monitor import (
    ExecutionMonitor
)


from app.ai.control_plane.intelligence_manager import (
    IntelligenceManager
)



__version__ = "1.0"