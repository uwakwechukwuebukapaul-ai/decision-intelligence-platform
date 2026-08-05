from .investigation_session import InvestigationSession
from .execution_context import ExecutionContext
from .agent_loop import AgentLoop
from .decision_memory import DecisionMemory



class AutonomousInvestigationRuntime:
    """
    Sentinel DNA autonomous investigation control plane.

    Connects:
    - Agents
    - Reasoning
    - Memory
    - Decisions
    """


    def __init__(self):

        self.agent_loop = AgentLoop()

        self.memory = DecisionMemory()

        self.sessions = {}



    def investigate(
        self,
        event
    ):


        session = InvestigationSession(
            event
        )


        context = ExecutionContext(
            session
        )


        results = self.agent_loop.execute(
            context
        )


        session.add_finding(

            {
                "type": "runtime_analysis",

                "results": results

            }

        )


        session.complete()


        self.memory.remember(

            {

                "event": event,

                "results": results

            }

        )


        self.sessions[
            session.session_id
        ] = session



        return session.to_dict()



    def get_session(
        self,
        session_id
    ):

        session = self.sessions.get(
            session_id
        )


        if session:

            return session.to_dict()


        return None