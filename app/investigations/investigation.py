"""
Sentinel DNA Investigation Object

Represents a complete security investigation.
"""

from datetime import datetime
from .investigation_state import InvestigationState



class Investigation:


    def __init__(
        self,
        investigation_id,
        case_id=None,
        evidence=None
    ):

        self.investigation_id = investigation_id

        self.case_id = case_id

        self.evidence = evidence or []

        self.state = InvestigationState(
            investigation_id
        )

        self.created_at = datetime.utcnow()



    def add_agent(
        self,
        agent_name
    ):

        self.state.register_agent(
            agent_name
        )



    def start(self):

        self.state.start()



    def add_finding(
        self,
        finding
    ):

        self.state.add_finding(
            finding
        )



    def complete(self):

        self.state.complete()



    def report(self):

        return {

            "investigation_id":
                self.investigation_id,

            "case_id":
                self.case_id,

            "evidence_count":
                len(self.evidence),

            "state":
                self.state.to_dict()

        }