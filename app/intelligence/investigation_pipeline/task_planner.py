"""
Sentinel DNA
Task Planner

Creates intelligence execution tasks
for investigations.
"""


class TaskPlanner:


    def create_tasks(
        self,
        investigation,
    ):

        tasks = []


        if investigation.evidence:

            tasks.append(
                {
                    "capability":
                        "threat_intelligence"
                }
            )


        tasks.append(
            {
                "capability":
                    "risk_scoring"
            }
        )


        tasks.append(
            {
                "capability":
                    "mitre_mapping"
            }
        )


        return tasks