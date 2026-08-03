from datetime import datetime

from app.ai.planning.goal_decomposer import GoalDecomposer
from app.ai.planning.task_generator import TaskGenerator
from app.ai.planning.execution_planner import ExecutionPlanner
from app.ai.planning.plan_memory import PlanMemory



class PlanningEngine:


    def __init__(self):

        self.goals = GoalDecomposer()

        self.tasks = TaskGenerator()

        self.execution = ExecutionPlanner()

        self.memory = PlanMemory()



    def create_plan(

        self,

        mission,

        intelligence=[]

    ):


        goal_result = self.goals.decompose(
            mission
        )


        task_result = self.tasks.generate(
            goal_result["goals"]
        )


        execution_result = self.execution.create_execution_plan(
            task_result["tasks"]
        )


        plan = {

            "mission":
                mission,

            "intelligence":
                intelligence,

            "goals":
                goal_result["goals"],

            "tasks":
                task_result["tasks"],

            "execution":
                execution_result,

            "confidence":
                90

        }


        stored = self.memory.store(
            plan
        )


        return {

            "status":
                "completed",

            "planning":
                stored,

            "timestamp":
                datetime.utcnow().isoformat()

        }