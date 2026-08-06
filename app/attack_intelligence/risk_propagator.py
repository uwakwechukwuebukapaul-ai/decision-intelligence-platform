class RiskPropagator:


    def calculate(
        self,
        steps
    ):


        risk_level = "medium"

        blast_radius = "medium"


        if len(steps) >= 4:

            risk_level = "critical"

            blast_radius = "high"


        return {

            "risk_level": risk_level,

            "blast_radius": blast_radius

        }