from .playbook import PlaybookEngine
from .action_executor import ActionExecutor
from .response_workflow import ResponseWorkflow



class AutomationEngine:
    """
    Autonomous SOAR execution engine.
    """


    def __init__(self):

        self.playbooks = PlaybookEngine()

        self.executor = ActionExecutor()

        self.workflow = ResponseWorkflow()



    def respond(
        self,
        threat_type,
        incident
    ):


        playbook = self.playbooks.select(
            threat_type
        )


        workflow = self.workflow.create_workflow(
            incident
        )


        results = []


        for action in playbook["actions"]:

            results.append(

                self.executor.execute(
                    action
                )

            )


        return {

            "incident":
            incident,


            "playbook":
            playbook["name"],


            "workflow":
            workflow,


            "actions":
            results,


            "status":
            "completed"

        }