from datetime import datetime

from .user_manager import UserManager
from .role_manager import RoleManager
from .permission_engine import PermissionEngine
from .session_manager import SessionManager
from .tenant_manager import TenantManager
from .access_policy import AccessPolicy
from .identity_logger import IdentityLogger
from .identity_memory import IdentityMemory


class IdentityManagementEngine:

    def __init__(self):

        self.users = UserManager()
        self.roles = RoleManager()
        self.permissions = PermissionEngine()
        self.sessions = SessionManager()
        self.tenants = TenantManager()
        self.policy = AccessPolicy()
        self.logger = IdentityLogger()
        self.memory = IdentityMemory()


    def authenticate_user(self, username, role="SOC Analyst"):

        user = self.users.create_user(username)

        role_info = self.roles.assign_role(
            username,
            role
        )

        permissions = self.permissions.get_permissions(
            role
        )

        session = self.sessions.create_session(
            username
        )

        tenant = self.tenants.assign_tenant(
            username
        )

        policy = self.policy.evaluate(
            role
        )

        memory = self.memory.store(
            username
        )

        log = self.logger.record(
            username
        )


        return {

            "status": "completed",

            "user": user,

            "role": role_info,

            "permissions": permissions,

            "session": session,

            "tenant": tenant,

            "access_policy": policy,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.utcnow().isoformat()
        }