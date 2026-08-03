from datetime import datetime



class PerformanceAnalyzer:


    def analyze(
        self,
        agent_id,
        execution_results
    ):

        completed = 0
        total = len(execution_results)


        for result in execution_results:

            if result.get("status") == "completed":

                completed += 1



        success_rate = 0


        if total > 0:

            success_rate = int(
                (completed / total) * 100
            )



        return {

            "agent_id":
                agent_id,

            "performance":

                {

                    "total_tasks":
                        total,

                    "completed_tasks":
                        completed,

                    "success_rate":
                        success_rate

                },


            "recommendations":

                self.generate_recommendations(
                    success_rate
                ),


            "timestamp":
                datetime.utcnow().isoformat()

        }



    def generate_recommendations(
        self,
        success_rate
    ):


        recommendations = []


        if success_rate < 70:

            recommendations.append(
                "Improve reasoning accuracy"
            )


        if success_rate >= 70:

            recommendations.append(
                "Expand current capabilities"
            )


        recommendations.append(
            "Continue learning from mission experience"
        )


        return recommendations