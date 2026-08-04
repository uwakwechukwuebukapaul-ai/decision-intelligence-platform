class AutomationRules:


    def evaluate(self, incident):

        incident_lower = incident.lower()

        actions = []


        if "ransomware" in incident_lower:

            actions.extend(
                [
                    "isolate_host",
                    "block_indicator",
                    "create_investigation"
                ]
            )


        if "credential" in incident_lower:

            actions.append(
                "disable_account"
            )


        if "powershell" in incident_lower:

            actions.append(
                "collect_endpoint_artifacts"
            )


        return actions