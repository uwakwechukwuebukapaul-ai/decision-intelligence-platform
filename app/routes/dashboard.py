import json

from flask import Blueprint, render_template

from app.database.db import SessionLocal

from app.models.user import UserProfile
from app.models.report import AIReport



dashboard_bp = Blueprint(
    "dashboard",
    __name__
)




@dashboard_bp.route(
    "/dashboard/<int:user_id>"
)
def dashboard(user_id):


    db = SessionLocal()



    try:


        user = db.query(UserProfile).filter(
            UserProfile.id == user_id
        ).first()



        if not user:


            return "User not found"







        reports = db.query(AIReport).filter(

            AIReport.user_id == user_id

        ).order_by(

            AIReport.id.desc()

        ).all()






        intelligence = {

            "readiness": {},

            "evolution": {},

            "simulation": {},

            "mentor": {},

            "learning": {}

        }







        for report in reports:


            report.report_content = json.loads(

                report.report_content

            )



            content = report.report_content





            # ===============================
            # Extract AI Intelligence Modules
            # ===============================


            if content.get("readiness"):

                intelligence["readiness"] = (
                    content["readiness"]
                )



            if content.get("evolution"):

                intelligence["evolution"] = (
                    content["evolution"]
                )



            if content.get("simulation"):

                intelligence["simulation"] = (
                    content["simulation"]
                )



            if content.get("mentor"):

                intelligence["mentor"] = (
                    content["mentor"]
                )



            if content.get("learning"):

                intelligence["learning"] = (
                    content["learning"]
                )









        return render_template(

            "dashboard/index.html",

            user=user,

            reports=reports,

            intelligence=intelligence

        )







    except Exception as error:


        return {

            "error": str(error)

        }, 500






    finally:


        db.close()