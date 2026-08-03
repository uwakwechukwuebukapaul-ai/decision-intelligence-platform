from datetime import datetime

from app.ai.orchestration.agent_selector import AgentSelector
from app.ai.orchestration.workflow_engine import WorkflowEngine
from app.ai.orchestration.decision_pipeline import DecisionPipeline

from app.ai.runtime.execution_manager import ExecutionManager



class Orchestrator:


    def __init__(self):

        self.agent_selector = AgentSelector()

        self.workflow_engine = WorkflowEngine()

        self.pipeline = DecisionPipeline()

        self.execution_manager = ExecutionManager()



    def execute(
        self,
        mission_id,
        objective
    ):


        agents = self.agent_selector.select_agents(
            objective
        )


        workflow = self.workflow_engine.create_workflow(
            mission_id,
            agents
        )


        execution = self.execution_manager.execute_agents(

            agents,

            objective

        )


        result = self.pipeline.run(

            mission_id,

            objective,

            agents

        )


        return {

            "orchestrator":
                "active",

            "mission_id":
                mission_id,

            "objective":
                objective,

            "agents":
                agents,

            "workflow":
                workflow,

            "execution":
                execution,

            "result":
                result,

            "status":
                "completed",

            "timestamp":
                datetime.utcnow().isoformat()

        }