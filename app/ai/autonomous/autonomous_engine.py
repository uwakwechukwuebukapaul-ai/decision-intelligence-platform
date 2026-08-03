from datetime import datetime

from app.ai.autonomous.intelligence_cycle import IntelligenceCycle



class AutonomousEngine:


    def __init__(self):

        self.cycle = IntelligenceCycle()



    def execute_cycle(

        self,

        agent_id,

        mission_id,

        execution_results

    ):


        result = self.cycle.run(

            agent_id,

            mission_id,

            execution_results

        )


        return {

            "autonomous_engine":
                "active",

            "result":
                result,

            "timestamp":
                datetime.utcnow().isoformat()

        }