"""
Sentinel DNA Autonomous SOAR Engine

Provides:
- Security playbooks
- Automated response execution
- Workflow orchestration
- Approval management
- Integration actions
- SOAR memory
"""

from .soar_engine import SOAREngine

__all__ = [
    "SOAREngine"
]