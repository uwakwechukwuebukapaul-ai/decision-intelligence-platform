from .action_executor import ActionExecutor
from .playbook_manager import PlaybookManager
from .soar_repository import SOARRepository
from .soar_schema import create_execution



class SOAREngine:


    def __init__(self):

        self.executor = ActionExecutor()

        self.playbooks = PlaybookManager()

        self.repository = SOARRepository()



    def execute(
        self,
        incident
    ):

        incident_id = incident.get(
            "incident_id"
        )


        playbook = self.playbooks.select_playbook(
            incident
        )


        actions = self.playbooks.get_playbook(
            playbook
        )


        results = self.executor.execute_actions(

            actions,

            incident

        )


        execution = create_execution(

            incident_id,

            playbook,

            results,

            "executed"

        )


        return self.repository.save(
            execution
        )



    def history(self):

        return self.repository.get_all()