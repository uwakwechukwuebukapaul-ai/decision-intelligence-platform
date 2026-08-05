class HuntPlanner:

    def create_plan(self, threat):

        return {
            "threat": threat,
            "steps": [
                "collect telemetry",
                "analyze behavior",
                "identify anomalies"
            ]
        }


    def prioritize(self, hunts):

        return hunts