class LearningEngine:
    """
    Converts investigation history
    into intelligence improvements.
    """

    def learn(
        self,
        memory
    ):

        patterns = memory.patterns


        confidence = "LOW"


        if len(patterns) >= 3:

            confidence = "HIGH"


        elif len(patterns) > 0:

            confidence = "MEDIUM"



        learning = {

            "known_patterns":
                patterns,

            "confidence_upgrade":
                confidence,

            "recommendation":

                "Increase detection priority"
                if patterns
                else
                "Maintain baseline monitoring"

        }


        memory.update_learning(
            learning
        )


        return learning