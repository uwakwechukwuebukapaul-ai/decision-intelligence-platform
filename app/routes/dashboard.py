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


    user = db.query(UserProfile).filter(
        UserProfile.id == user_id
    ).first()


    if not user:

        db.close()

        return "User not found"



    reports = db.query(AIReport).filter(
        AIReport.user_id == user_id
    ).order_by(
        AIReport.created_at.desc()
    ).all()



    db.close()


    return render_template(
        "dashboard/index.html",
        user=user,
        reports=reports
    )