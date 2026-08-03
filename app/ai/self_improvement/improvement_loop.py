from app.ai.self_improvement.performance_analyzer import PerformanceAnalyzer
from app.ai.self_improvement.capability_upgrader import CapabilityUpgrader



class ImprovementLoop:


    def __init__(self):

        self.analyzer = PerformanceAnalyzer()

        self.upgrader = CapabilityUpgrader()



    def improve(

        self,

        agent_id,

        execution_results

    ):


        analysis = self.analyzer.analyze(

            agent_id,

            execution_results

        )


        upgrade = self.upgrader.upgrade(

            agent_id,

            analysis["recommendations"]

        )


        return {

            "agent_id":
                agent_id,

            "analysis":
                analysis,

            "upgrade":
                upgrade,

            "status":
                "improved"

        }