class RecommendationEngine:
    """
    Provides analyst response recommendations.
    """

    def generate(self, context):

        recommendations = []

        if context:
            recommendations.append(
                "Perform deeper investigation using available evidence."
            )

        else:
            recommendations.append(
                "Collect additional security context."
            )

        return {
            "recommendations": recommendations,
            "priority": "medium"
        }