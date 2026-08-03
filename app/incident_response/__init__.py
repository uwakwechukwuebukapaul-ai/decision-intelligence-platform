"""
Sentinel DNA Incident Response Platform

Capabilities:
- Incident creation
- Case management
- Evidence tracking
- Timeline reconstruction
- Analyst workflow
- Severity classification
- Automated reporting
"""

from .incident_engine import IncidentEngine

__all__ = [
    "IncidentEngine"
]