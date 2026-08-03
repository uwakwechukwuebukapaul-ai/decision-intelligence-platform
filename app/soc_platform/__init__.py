"""
Sentinel DNA AI SOC Command Center

Central SOC orchestration layer.

Capabilities:
- Alert management
- Case orchestration
- Investigation coordination
- Response planning
- Analyst dashboard intelligence
"""

from .soc_engine import SOCEngine

__all__ = [
    "SOCEngine"
]