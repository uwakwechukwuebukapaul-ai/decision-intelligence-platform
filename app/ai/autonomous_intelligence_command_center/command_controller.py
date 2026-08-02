from datetime import datetime

from .command_state import CommandState
from .command_orchestrator import CommandOrchestrator
from .command_executor import CommandExecutor



class CommandController:


    def __init__(self, user_id):

        self.user_id = user_id



    def execute_command_cycle(self):


        command_state = CommandState(
            self.user_id
        ).generate()



        orchestration = CommandOrchestrator().orchestrate()



        execution = CommandExecutor().execute()



        return {


            "user_id":

                self.user_id,



            "command_status":

                "active",



            "command_score":

                99,



            "command_state":

                command_state,



            "orchestration":

                orchestration,



            "execution":

                execution,



            "generated_at":

                datetime.utcnow().isoformat(),



            "version":

                "1.0"

        }