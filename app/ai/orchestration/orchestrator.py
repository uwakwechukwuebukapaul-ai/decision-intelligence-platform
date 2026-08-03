from datetime import datetime


class Orchestrator:
    """
    Central intelligence coordination layer.

    Responsible for:
    - receiving missions
    - routing tasks
    - selecting agents
    - creating workflows
    - executing decision pipelines
    """


    def __init__(self):

        self.status = "active"


        try:
            from app.ai.orchestration.task_router import TaskRouter
            self.task_router = TaskRouter()

        except Exception:
            self.task_router = None



        try:
            from app.ai.orchestration.agent_selector import AgentSelector
            self.agent_selector = AgentSelector()

        except Exception:
            self.agent_selector = None



        try:
            from app.ai.orchestration.workflow_engine import WorkflowEngine
            self.workflow_engine = WorkflowEngine()

        except Exception:
            self.workflow_engine = None



        try:
            from app.ai.orchestration.decision_pipeline import DecisionPipeline
            self.pipeline = DecisionPipeline()

        except Exception:
            self.pipeline = None



    def execute(
        self,
        mission_id,
        objective
    ):


        task = {

            "mission_id": mission_id,

            "objective": objective,

            "created_at":
                datetime.utcnow().isoformat()

        }



        if self.task_router:

            try:

                task["route"] = (
                    self.task_router.route(
                        objective
                    )
                )

            except Exception:

                task["route"] = "general"



        if self.agent_selector:

            try:

                agents = (
                    self.agent_selector.select_agents(
                        objective
                    )
                )

            except Exception:

                agents = []

        else:

            agents = []



        if self.workflow_engine:

            try:

                workflow = (
                    self.workflow_engine.create_workflow(
                        mission_id,
                        agents
                    )
                )

            except Exception:

                workflow = None

        else:

            workflow = None



        if self.pipeline:

            try:

                result = (
                    self.pipeline.run(
                        mission_id,
                        objective,
                        agents
                    )
                )

            except Exception:

                result = {

                    "message":
                        "Pipeline execution unavailable"

                }

        else:

            result = {

                "message":
                    "Decision pipeline unavailable"

            }



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


            "result":

                result,


            "status":

                "completed",


            "timestamp":

                datetime.utcnow().isoformat()

        }