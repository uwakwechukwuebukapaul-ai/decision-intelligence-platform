class ReasoningEngine:


    def analyze(
        self,
        intelligence
    ):


        reasons = []

        severity = intelligence.get(
            "severity",
            "unknown"
        )


        if severity == "critical":

            reasons.append(
                "Critical threat indicators identified"
            )


        if intelligence.get("indicator"):

            reasons.append(
                "IOC requires investigation"
            )


        if not reasons:

            reasons.append(
                "Insufficient evidence"
            )


        return reasons