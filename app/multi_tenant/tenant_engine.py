from datetime import datetime
import uuid

from .organization_manager import OrganizationManager
from .user_manager import UserManager
from .role_manager import RoleManager
from .permission_engine import PermissionEngine
from .data_isolation import DataIsolation
from .tenant_memory import TenantMemory



class TenantEngine:
    """
    Sentinel DNA Enterprise Multi-Tenant Engine.
    """


    def __init__(self):

        self.organizations = OrganizationManager()

        self.users = UserManager()

        self.roles = RoleManager()

        self.permissions = PermissionEngine()

        self.isolation = DataIsolation()

        self.memory = TenantMemory()



    def create_tenant(
        self,
        organization_name
    ):


        tenant = {


            "tenant_id":
                "TEN-" + uuid.uuid4().hex[:8].upper(),


            "organization":
                self.organizations.create(
                    organization_name
                ),


            "status":
                "ACTIVE",


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(tenant)


        return tenant



    def onboard_user(
        self,
        tenant_id,
        name,
        email,
        role
    ):


        user = self.users.create_user(
            name,
            email,
            role
        )


        return {

            "tenant_id":
                tenant_id,

            "user":
                user,

            "permissions":
                self.permissions.get_permissions(role)

        }