from flask import Blueprint, jsonify


from app.ai.orchestrator.orchestrator_engine import (
    run_ai_orchestrator
)



orchestrator_bp = Blueprint(
    "orchestrator",
    __name__
)




@orchestrator_bp.route(
    "/intelligence-center/<int:user_id>",
    methods=["GET"]
)

def intelligence_center(user_id):


    user_intelligence = {


        "user":{


            "id":user_id,

            "name":"Paul"

        },


        "career":{


            "target":
            "SOC Analyst"

        },


        "readiness":{


            "score":60,

            "level":
            "Developing"

        },


        "recommendations":{


            "next_focus":[

                "SIEM",

                "Detection Engineering"

            ]

        }

    }



    result = run_ai_orchestrator(

        user_intelligence,


        advisor={

            "message":
            "Improve enterprise SOC skills"

        },


        mentor={

            "message":
            "Keep building practical labs"

        },


        coach={

            "stage":
            "Foundation Building"

        },


        recommendation={

            "labs":[

                "SOC Lab",

                "SIEM Detection"

            ]

        },


        decision={

            "decision":
            "Focus on SIEM next"

        },


        career_report={

            "career":
            "SOC Analyst"

        }

    )



    return jsonify(result)