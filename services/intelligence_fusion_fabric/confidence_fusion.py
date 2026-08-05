class ConfidenceFusion:

    def calculate(self, scores):

        if not scores:

            return 0


        return sum(scores) / len(scores)


    def fuse(self, intelligence):

        confidence = intelligence.get(
            "confidence",
            []
        )

        return {
            "confidence_score": self.calculate(confidence)
        }