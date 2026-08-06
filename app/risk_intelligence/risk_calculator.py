class RiskCalculator:


    def calculate(self, data):

        score = 0

        factors = []


        if data.get("severity") == "critical":

            score += 40

            factors.append(
                "Critical threat severity"
            )


        if data.get("indicator"):

            score += 20

            factors.append(
                "Malicious indicator detected"
            )


        if data.get("asset_risk") == "critical":

            score += 20

            factors.append(
                "Critical asset exposure"
            )


        if data.get("identity_risk") == "critical":

            score += 20

            factors.append(
                "Critical identity exposure"
            )


        return {

            "score": score,

            "factors": factors

        }