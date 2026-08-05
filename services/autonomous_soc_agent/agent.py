from .task_planner import TaskPlanner
from .action_executor import ActionExecutor
from .agent_memory import AgentMemory



class AutonomousSOC_Agent:
    """
    Sentinel DNA Autonomous SOC Agent.

    Acts as an AI security teammate.
    """

    def __init__(self):

        self.planner = TaskPlanner()

        self.executor = ActionExecutor()

        self.memory = AgentMemory()



    def investigate(
        self,
        objective
    ):

        plan = self.planner.create_plan(
            objective
        )


        self.memory.remember(

            objective,

            plan

        )


        return {

            "agent":
                "sentinel_dna_autonomous_soc_agent",

            "objective":
                objective,

            "investigation_plan":
                plan,

            "status":
                "investigation_started"

        }



    def execute_action(
        self,
        action
    ):

        result = self.executor.execute(
            action
        )


        self.memory.remember(

            action,

            result

        )


        return result