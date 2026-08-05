class ConfidenceModel:

    def calculate(self, prediction):

        if prediction.get("risk") == "high":
            return 0.9

        if prediction.get("risk") == "medium":
            return 0.75

        return 0.5