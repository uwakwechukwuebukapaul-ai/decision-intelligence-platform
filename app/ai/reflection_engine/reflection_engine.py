from datetime import datetime

from .reasoning_analyzer import analyze_reasoning
from .lesson_extractor import extract_lessons
from .evolution_planner import create_evolution_plan



def run_reflection(user_id):

    reasoning = analyze_reasoning(user_id)

    lessons = extract_lessons(user_id)

    evolution = create_evolution_plan(user_id)


    return {


        "user_id":

            user_id,


        "reflection_status":

            "completed",


        "generated_at":

            datetime.utcnow().isoformat(),


        "reasoning_analysis":

            reasoning,


        "lessons_extracted":

            lessons,


        "evolution_plan":

            evolution,


        "reflection_score":

            98,


        "version":

            "1.0"

    }