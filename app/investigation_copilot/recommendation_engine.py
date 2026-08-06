class RecommendationEngine:


    def generate(self, context):

        actions = []


        if context.get("indicator"):

            actions.append(
                "Block malicious indicator"
            )


        if context.get("asset"):

            actions.append(
                "Investigate affected asset"
            )


        if context.get("identity"):

            actions.append(
                "Review identity activity"
            )


        if context.get("severity") == "critical":

            actions.append(
                "Execute incident response workflow"
            )


        return actions