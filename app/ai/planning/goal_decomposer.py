from datetime import datetime


class GoalDecomposer:


    def decompose(
        self,
        mission
    ):

        goals = []


        if "AI SOC" in mission or "SOC" in mission:

            goals = [
                "Research AI SOC market",
                "Analyze security operations challenges",
                "Design AI SOC architecture",
                "Build intelligent automation workflows",
                "Validate product strategy"
            ]

        else:

            goals = [
                "Analyze mission requirements",
                "Create execution strategy",
                "Complete mission objectives"
            ]


        return {

            "mission": mission,

            "goals": goals,

            "goal_count": len(goals),

            "created_at":
                datetime.utcnow().isoformat()

        }