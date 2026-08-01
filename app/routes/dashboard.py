from flask import Blueprint, render_template

from app.database.db import SessionLocal
from app.models.user import UserProfile

from app.ai.decision_engine import analyze_profile
from app.reports.report_generator import generate_report


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)



@dashboard_bp.route("/dashboard/<int:user_id>")
def dashboard(user_id):

    db = SessionLocal()


    user = db.query(UserProfile).filter(
        UserProfile.id == user_id
    ).first()


    if not user:

        db.close()

        return "User not found"


    analysis = analyze_profile(user)


    report = generate_report(
        user,
        analysis
    )


    db.close()


    return render_template(
        "dashboard/index.html",
        report=report
    )