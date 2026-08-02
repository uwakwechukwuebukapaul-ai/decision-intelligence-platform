"""
Autonomous Operating System Intelligence Layer

Provides the control plane for:
- Intelligence lifecycle management
- Agent scheduling
- Decision execution
- Resource allocation
- Continuous learning

Version: 1.0
"""

from .system_kernel import SystemKernel
from .intelligence_scheduler import IntelligenceScheduler

__all__ = [
    "SystemKernel",
    "IntelligenceScheduler"
]