from datetime import datetime

from app.ai.execution.action_manager import ActionManager
from app.ai.execution.workflow_runner import WorkflowRunner
from app.ai.execution.execution_monitor import ExecutionMonitor
from app.ai.execution.result_evaluator import ResultEvaluator
from app.ai.execution.execution_memory import ExecutionMemory



class ExecutionEngine:


    def __init__(self):

        self.actions = ActionManager()

        self.runner = WorkflowRunner()

        self.monitor = ExecutionMonitor()

        self.evaluator = ResultEvaluator()

        self.memory = ExecutionMemory()



    def execute(
        self,
        plan
    ):


        tasks = plan.get(
            "tasks",
            []
        )


        action_result = self.actions.create_actions(
            tasks
        )


        workflow = self.runner.run(
            action_result["actions"]
        )


        monitoring = self.monitor.monitor(
            workflow
        )


        evaluation = self.evaluator.evaluate(
            workflow
        )


        execution = {

            "mission":
                plan.get("mission"),

            "actions":
                action_result,

            "workflow":
                workflow,

            "monitoring":
                monitoring,

            "evaluation":
                evaluation

        }


        stored = self.memory.store(
            execution
        )


        return {

            "status":
                "completed",

            "execution":
                stored,

            "timestamp":
                datetime.utcnow().isoformat()

        }