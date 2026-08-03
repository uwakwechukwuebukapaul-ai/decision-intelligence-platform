from datetime import datetime


class ReasoningChain:
    """
    Builds explainable reasoning chains.

    Enterprise AI systems should expose
    decision justification without exposing
    private model internals.
    """

    def build(self, context):

        reasoning = []

        text = context.lower()

        if "ransomware" in text:
            reasoning.append(
                "Ransomware activity identified"
            )

        if "server" in text or "endpoint" in text:
            reasoning.append(
                "Critical infrastructure asset affected"
            )

        if "finance" in text:
            reasoning.append(
                "High business impact asset detected"
            )

        if not reasoning:
            reasoning.append(
                "General security assessment performed"
            )

        return {
            "reasoning_steps": reasoning,
            "timestamp": datetime.utcnow().isoformat()
        }