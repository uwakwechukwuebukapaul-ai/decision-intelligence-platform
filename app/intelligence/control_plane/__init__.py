"""
Intelligence Control Plane

Central governance layer for autonomous intelligence execution.
"""

from .intelligence_controller import IntelligenceController

from .task_manager import (
    TaskManager,
    IntelligenceTask,
)

from .policy_engine import PolicyEngine

from .capability_manager import CapabilityManager

from .audit_logger import AuditLogger

from .health_monitor import HealthMonitor

from .runtime_metrics import RuntimeMetrics


# Backward compatibility alias
# Existing routes expect AuditManager
AuditManager = AuditLogger


__all__ = [

    "IntelligenceController",

    "TaskManager",

    "IntelligenceTask",

    "PolicyEngine",

    "CapabilityManager",

    "AuditLogger",

    "AuditManager",

    "HealthMonitor",

    "RuntimeMetrics",

]