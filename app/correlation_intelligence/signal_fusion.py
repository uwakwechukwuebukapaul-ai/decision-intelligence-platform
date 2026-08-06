class SignalFusion:


    def calculate(self, data):

        score = 0


        signals = []


        if data.get("severity") == "critical":

            score += 30

            signals.append(
                "Critical threat severity"
            )


        if data.get("indicator"):

            score += 25

            signals.append(
                "Malicious indicator detected"
            )


        if data.get("asset"):

            score += 25

            signals.append(
                "Asset exposure identified"
            )


        if data.get("identity"):

            score += 20

            signals.append(
                "Identity risk detected"
            )


        return {

            "risk_score": min(score,100),

            "signals": signals

        }