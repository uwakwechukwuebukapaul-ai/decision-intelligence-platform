from flask import Blueprint, jsonify

from datetime import datetime


from app.ai.intelligence_governance.governance_controller import (
    GovernanceController
)

from app.ai.intelligence_governance.policy_engine import (
    PolicyEngine
)

from app.ai.intelligence_governance.safety_monitor import (
    SafetyMonitor
)

from app.ai.intelligence_governance.alignment_engine import (
    AlignmentEngine
)

from app.ai.intelligence_governance.trust_manager import (
    TrustManager
)

from app.ai.intelligence_governance.audit_intelligence import (
    AuditIntelligence
)



intelligence_governance_bp = Blueprint(

    "intelligence_governance",

    __name__

)



@intelligence_governance_bp.route(

    "/intelligence-governance/<int:user_id>",

    methods=["GET"]

)

def intelligence_governance(user_id):


    governance = GovernanceController()

    policy = PolicyEngine()

    safety = SafetyMonitor()

    alignment = AlignmentEngine()

    trust = TrustManager()

    audit = AuditIntelligence()



    response = {


        "status":

            "operational",



        "user_id":

            user_id,



        "intelligence_governance":

            {


                "generated_at":

                    datetime.utcnow().isoformat(),



                "governance":

                    governance.evaluate(user_id),



                "policy":

                    policy.evaluate(),



                "safety":

                    safety.monitor(),



                "alignment":

                    alignment.validate(),



                "trust":

                    trust.calculate(),



                "audit":

                    audit.generate(),



                "overall_score":

                    99,



                "version":

                    "1.0"

            }

    }



    return jsonify(response)