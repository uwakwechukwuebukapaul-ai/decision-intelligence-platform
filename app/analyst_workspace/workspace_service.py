"""
Analyst Workspace Service

Combines investigation intelligence
into analyst-ready workspace data.
"""


from .investigation_summary import (
    InvestigationSummaryGenerator,
)

from .evidence_view import (
    EvidenceView,
)

from .analyst_actions import (
    AnalystActionTracker,
)



class AnalystWorkspaceService:
    """
    Builds SOC analyst workspace objects
    from investigation intelligence.
    """


    def __init__(self):

        self.summary = InvestigationSummaryGenerator()

        self.evidence = EvidenceView()

        self.actions = AnalystActionTracker()



    def build_workspace(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Generate analyst workspace data.
        """


        return {

            "summary":
                self.summary.generate(
                    intelligence
                ),

            "evidence":
                self.evidence.build(
                    intelligence
                ),

            "actions":
                self.actions.history(),

        }