from datetime import datetime

from .authentication_engine import AuthenticationEngine
from .mfa_engine import MFAEngine
from .sso_manager import SSOManager
from .oauth_manager import OAuthManager
from .api_key_manager import APIKeyManager
from .session_manager import SessionManager
from .zero_trust_engine import ZeroTrustEngine
from .identity_memory import IdentityMemory



class IdentityEngine:
    """
    Sentinel DNA Enterprise Identity Engine.
    """


    def __init__(self):

        self.authentication = AuthenticationEngine()

        self.mfa = MFAEngine()

        self.sso = SSOManager()

        self.oauth = OAuthManager()

        self.api_keys = APIKeyManager()

        self.sessions = SessionManager()

        self.zero_trust = ZeroTrustEngine()

        self.memory = IdentityMemory()



    def secure_identity(
        self,
        username
    ):


        auth = self.authentication.authenticate(
            username
        )


        mfa = self.mfa.verify(
            username
        )


        session = self.sessions.create_session(
            username
        )


        zero_trust = self.zero_trust.evaluate(
            username,
            "corporate-device",
            20
        )


        result = {

            "status":
                "completed",

            "identity":
                username,

            "authentication":
                auth,

            "mfa":
                mfa,

            "session":
                session,

            "zero_trust":
                zero_trust,

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(result)


        return result