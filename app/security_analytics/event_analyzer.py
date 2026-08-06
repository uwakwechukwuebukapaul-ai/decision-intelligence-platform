class EventAnalyzer:


    def analyze(self, event):

        findings = []

        score = 0


        if event.get("severity") == "critical":

            score += 40

            findings.append(
                "Critical security event detected"
            )


        if event.get("indicator"):

            score += 30

            findings.append(
                "Threat indicator associated"
            )


        if event.get("source"):

            score += 10

            findings.append(
                "Event source identified"
            )


        return {

            "score": score,

            "findings": findings

        }