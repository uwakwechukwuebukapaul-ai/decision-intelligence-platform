from .identity_repository import IdentityRepository
from .identity_schema import IdentitySchema
from .risk_analyzer import IdentityRiskAnalyzer



class IdentityEngine:


    def __init__(self):

        self.repository = IdentityRepository()

        self.analyzer = IdentityRiskAnalyzer()



    def register_identity(
        self,
        username,
        role,
        department,
        privilege_level
    ):


        identity = IdentitySchema.create(
            username,
            role,
            department,
            privilege_level
        )


        self.repository.save(identity)


        risk = self.analyzer.analyze(identity)


        return {

            "identity": identity,

            "risk": risk

        }