"""
Sentinel DNA Enterprise Gateway Layer

Central integration gateway connecting:
- Autonomous Brain
- SOC Platform
- Threat Intelligence
- Detection Engine
- Incident Response
- Threat Hunting
- Copilot
"""

from .api_gateway import APIGateway

__all__ = [
    "APIGateway"
]