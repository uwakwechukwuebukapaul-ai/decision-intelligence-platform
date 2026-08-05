class TaskPlanner:
    """
    Creates investigation plans
    from security objectives.
    """

    def create_plan(
        self,
        objective
    ):

        objective_text = objective.lower()


        tasks = []


        tasks.append(
            "Collect security evidence"
        )


        if "ransomware" in objective_text:

            tasks.append(
                "Analyze encryption behavior"
            )


            tasks.append(
                "Identify affected assets"
            )


        if "phishing" in objective_text:

            tasks.append(
                "Analyze email indicators"
            )


        tasks.extend(
            [
                "Perform threat intelligence lookup",

                "Map MITRE ATT&CK techniques",

                "Recommend response actions"
            ]
        )


        return {

            "objective":
                objective,

            "tasks":
                tasks,

            "plan_status":
                "created"

        }