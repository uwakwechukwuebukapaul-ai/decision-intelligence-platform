from datetime import datetime

from app.ai.evaluation_engine.scoring_engine import calculate_scores
from app.ai.evaluation_engine.quality_analyzer import analyze_quality
from app.ai.evaluation_engine.confidence_adjuster import adjust_confidence


def run_evaluation(user_id):

    scores = calculate_scores()

    quality = analyze_quality()

    confidence = adjust_confidence(
        scores["decision_quality_score"]
    )

    return {

        "user_id": user_id,

        "evaluation_status": "completed",

        "generated_at":
            datetime.utcnow().isoformat(),

        "scores":
            scores,

        "quality_analysis":
            quality,

        "confidence_adjustment":
            confidence,

        "version":
            "1.0"

    }