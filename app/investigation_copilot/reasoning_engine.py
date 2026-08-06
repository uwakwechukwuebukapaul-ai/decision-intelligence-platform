class ReasoningEngine:


    def analyze(self, context):

        findings = []


        if context.get("indicator"):

            findings.append(
                "Malicious indicator identified"
            )


        if context.get("asset"):

            findings.append(
                "Critical asset context available"
            )


        if context.get("identity"):

            findings.append(
                "Identity activity requires investigation"
            )


        if context.get("severity") == "critical":

            findings.append(
                "Critical severity incident detected"
            )


        return findings