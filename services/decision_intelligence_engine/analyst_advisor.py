class AnalystAdvisor:

    def advise(self, decision):

        return {
            "recommendation":
                f"Execute {decision.get('priority','P4')} response workflow",
            "reason":
                "Recommendation generated from risk and intelligence context"
        }