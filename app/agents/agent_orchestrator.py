from datetime import datetime

from .soc_agent import SOCAgent
from .research_agent import ResearchAgent
from .threat_hunting_agent import ThreatHuntingAgent
from .compliance_agent import ComplianceAgent
from .executive_agent import ExecutiveAgent
from .agent_memory import AgentMemory


class AgentOrchestrator:


    def __init__(self):

        self.soc = SOCAgent()
        self.research = ResearchAgent()
        self.hunting = ThreatHuntingAgent()
        self.compliance = ComplianceAgent()
        self.executive = ExecutiveAgent()

        self.memory = AgentMemory()



    def execute(self, request):


        soc_result = self.soc.investigate(request)

        research_result = self.research.research(
            request
        )

        hunting_result = self.hunting.hunt(
            "Enterprise Environment"
        )

        compliance_result = self.compliance.evaluate(
            request
        )

        executive_result = self.executive.advise(
            soc_result
        )


        final = {

            "status":
            "completed",

            "agent_pipeline":
            {

                "soc":
                soc_result,

                "research":
                research_result,

                "threat_hunting":
                hunting_result,

                "compliance":
                compliance_result,

                "executive":
                executive_result
            },

            "created_at":
            datetime.now().isoformat()

        }


        self.memory.store(
            "Agent Orchestrator",
            request,
            final
        )


        return final