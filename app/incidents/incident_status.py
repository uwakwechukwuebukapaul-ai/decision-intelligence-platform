"""
Sentinel DNA - Incident Status Management

Controls SOC incident lifecycle states.
"""


from enum import Enum





class IncidentStatus(str, Enum):
    """
    Enterprise SOC incident states.
    """

    OPEN = "open"

    TRIAGED = "triaged"

    INVESTIGATING = "investigating"

    CONTAINMENT = "containment"

    REMEDIATION = "remediation"

    CLOSED = "closed"