"""
Sentinel DNA Investigation State Engine

Tracks investigation lifecycle,
agent execution and findings.
"""

from enum import Enum
from datetime import datetime


class InvestigationStatus(Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class AgentStatus(Enum):
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class InvestigationState:

    def __init__(self, investigation_id):

        self.investigation_id = investigation_id

        self.status = InvestigationStatus.CREATED

        self.created_at = datetime.utcnow()

        self.updated_at = self.created_at

        self.agents = {}

        self.findings = []

        self.risk_score = 0


    def start(self):

        self.status = InvestigationStatus.RUNNING
        self.updated_at = datetime.utcnow()


    def complete(self):

        self.status = InvestigationStatus.COMPLETED
        self.updated_at = datetime.utcnow()


    def fail(self):

        self.status = InvestigationStatus.FAILED
        self.updated_at = datetime.utcnow()


    def register_agent(self, agent_name):

        self.agents[agent_name] = {
            "status": AgentStatus.WAITING.value,
            "started": None,
            "completed": None
        }


    def update_agent(
        self,
        agent_name,
        status
    ):

        if agent_name not in self.agents:
            self.register_agent(agent_name)


        self.agents[agent_name]["status"] = status.value

        if status == AgentStatus.RUNNING:
            self.agents[agent_name]["started"] = datetime.utcnow()


        if status in [
            AgentStatus.COMPLETED,
            AgentStatus.FAILED
        ]:
            self.agents[agent_name]["completed"] = datetime.utcnow()


        self.updated_at = datetime.utcnow()



    def add_finding(
        self,
        finding
    ):

        self.findings.append(
            {
                "finding": finding,
                "timestamp": datetime.utcnow()
            }
        )

        self.updated_at = datetime.utcnow()



    def set_risk_score(
        self,
        score
    ):

        self.risk_score = score

        self.updated_at = datetime.utcnow()



    def to_dict(self):

        return {

            "investigation_id":
                self.investigation_id,

            "status":
                self.status.value,

            "created_at":
                self.created_at.isoformat(),

            "updated_at":
                self.updated_at.isoformat(),

            "agents":
                self.agents,

            "findings":
                self.findings,

            "risk_score":
                self.risk_score
        }