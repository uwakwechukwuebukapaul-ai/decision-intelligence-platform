class TaskRouter:


    def route(
        self,
        incident
    ):

        tasks = []


        indicator = incident.get(
            "indicator",
            ""
        )


        if indicator:

            tasks.append(
                "threat_agent"
            )


            tasks.append(
                "detection_agent"
            )


            tasks.append(
                "evidence_agent"
            )


        if incident.get("user"):

            tasks.append(
                "identity_agent"
            )


        return tasks