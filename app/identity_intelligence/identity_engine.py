from datetime import datetime
import uuid

from .identity_repository import IdentityRepository
from .risk_analyzer import IdentityRiskAnalyzer



class IdentityEngine:


    def __init__(self):

        self.repository = IdentityRepository()

        self.risk = IdentityRiskAnalyzer()



    def analyze_identity(
        self,
        username,
        role,
        department="unknown",
        privilege_level="user"
    ):


        identity = {


            "identity_id":
            "ID-" + uuid.uuid4().hex[:8].upper(),


            "username":
            username,


            "role":
            role,


            "department":
            department,


            "privilege_level":
            privilege_level,


            "created_at":
            datetime.utcnow().isoformat()

        }


        identity["risk"] = self.risk.analyze(identity)


        self.repository.save(identity)


        return identity