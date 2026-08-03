"""
Sentinel DNA Enterprise Identity Security Framework

Provides:
- Identity management
- Authentication
- MFA
- SSO
- OAuth authorization
- API key security
- Session management
- Zero Trust enforcement
"""

from .identity_engine import IdentityEngine

__all__ = [
    "IdentityEngine"
]