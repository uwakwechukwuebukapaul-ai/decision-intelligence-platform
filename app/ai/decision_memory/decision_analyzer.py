from datetime import datetime


class DecisionAnalyzer:
    """
    Decision Analysis Intelligence Layer

    Responsibilities:
    - Analyze decision outcomes
    - Measure accuracy
    - Evaluate confidence calibration
    - Generate learning signals
    """


    def __init__(self):

        self.analysis_history = []



    def analyze_decisions(
        self,
        decisions
    ):

        total = len(decisions)


        if total == 0:

            return {

                "total_decisions": 0,

                "successful_decisions": 0,

                "accuracy": 0,

                "timestamp":
                    datetime.utcnow().isoformat()

            }



        successful = [

            decision

            for decision in decisions

            if decision.get("outcome") == "success"

        ]


        accuracy = round(

            (len(successful) / total) * 100,

            2

        )


        analysis = {

            "total_decisions":
                total,


            "successful_decisions":
                len(successful),


            "failed_decisions":
                total - len(successful),


            "accuracy":
                accuracy,


            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.analysis_history.append(
            analysis
        )


        return analysis



    def confidence_analysis(
        self,
        decisions
    ):


        high_confidence = []


        successful_high_confidence = []


        for decision in decisions:


            if decision.get(
                "confidence",
                0
            ) >= 70:


                high_confidence.append(
                    decision
                )


                if decision.get(
                    "outcome"
                ) == "success":


                    successful_high_confidence.append(
                        decision
                    )



        if len(high_confidence) == 0:

            accuracy = 0


        else:

            accuracy = round(

                (
                    len(successful_high_confidence)
                    /
                    len(high_confidence)
                )
                *
                100,

                2

            )



        return {

            "high_confidence_decisions":
                len(high_confidence),


            "successful_high_confidence":
                len(successful_high_confidence),


            "confidence_accuracy":
                accuracy

        }



    def generate_learning_signal(
        self,
        decisions
    ):


        analysis = self.analyze_decisions(
            decisions
        )


        confidence = self.confidence_analysis(
            decisions
        )


        recommendations = []



        if analysis["accuracy"] >= 80:

            recommendations.append(
                "Current decision strategy is performing well"
            )


        else:

            recommendations.append(
                "Improve reasoning before making decisions"
            )



        if confidence["confidence_accuracy"] >= 80:

            recommendations.append(
                "Confidence calibration is accurate"
            )


        else:

            recommendations.append(
                "Adjust confidence prediction model"
            )



        return {

            "analysis":
                analysis,


            "confidence":
                confidence,


            "learning_signals":
                recommendations,


            "timestamp":
                datetime.utcnow().isoformat()

        }