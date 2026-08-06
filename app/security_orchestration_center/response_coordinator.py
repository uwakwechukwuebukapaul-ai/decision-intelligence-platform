class ResponseCoordinator:

    def coordinate(self, incident):

        actions = []

        if incident["priority"] == "critical":

            actions.extend([
                "Execute SOAR containment",
                "Start autonomous investigation",
                "Notify SOC analyst"
            ])

        else:

            actions.append(
                "Perform investigation review"
            )

        return {
            "actions": actions,
            "response_status": "initiated"
        }