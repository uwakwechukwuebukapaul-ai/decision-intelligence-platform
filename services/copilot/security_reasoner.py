class SecurityReasoner:
    """
    Security analysis reasoning component.

    Converts analyst questions into
    investigation guidance.
    """


    def analyze(
        self,
        question
    ):

        question_lower = question.lower()


        recommendations = []


        if "ransomware" in question_lower:

            recommendations.extend(
                [
                    "Identify affected hosts",
                    "Check encryption activity",
                    "Review lateral movement indicators",
                    "Collect forensic evidence"
                ]
            )


        elif "phishing" in question_lower:

            recommendations.extend(
                [
                    "Analyze sender reputation",
                    "Extract malicious URLs",
                    "Check email headers",
                    "Block indicators"
                ]
            )


        else:

            recommendations.append(
                "Collect additional security telemetry"
            )


        return {

            "topic":
                "security investigation",

            "recommendations":
                recommendations,

            "confidence":
                0.85

        }