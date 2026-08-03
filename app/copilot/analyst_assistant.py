from datetime import datetime


class AnalystAssistant:
    """
    Provides SOC analyst assistance.
    """

    def assist(self, question):

        text = question.lower()


        recommendations = []


        if "alert" in text:

            recommendations.append(
                "Review alert evidence and indicators"
            )


        if "ransomware" in text:

            recommendations.extend(
                [
                    "Check affected endpoints",
                    "Review file encryption activity",
                    "Start containment process"
                ]
            )


        if not recommendations:

            recommendations.append(
                "Collect additional security evidence"
            )


        return {

            "analysis":
                "Security investigation assistance generated",

            "recommendations":
                recommendations,

            "timestamp":
                datetime.utcnow().isoformat()

        }