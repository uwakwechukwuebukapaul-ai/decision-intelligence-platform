"""
AI Career Advisor Package

This module contains the orchestration layer
that combines multiple AI intelligence engines:

- Career Planner Engine
- Recommendation Engine
- Skill Gap Intelligence
- Decision Intelligence

The advisor package provides unified career
guidance responses for users.
"""


from app.ai.advisor.career_advisor import (
    generate_career_advisor
)


__all__ = [
    "generate_career_advisor"
]