"""
Sentinel DNA Multi-Tenant Enterprise Layer

Provides:
- Tenant management
- Organization management
- User management
- RBAC permissions
- Data isolation
- Tenant memory
"""

from .tenant_engine import TenantEngine

__all__ = [
    "TenantEngine"
]