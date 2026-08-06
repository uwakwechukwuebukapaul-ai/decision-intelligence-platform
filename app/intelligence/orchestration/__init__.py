"""
Sentinel DNA - Investigation Orchestration Package

Central orchestration layer responsible for coordinating:

- Intelligence fusion
- Risk analysis
- Correlation
- Campaign detection
- Threat actor analysis
- AI reasoning
- Copilot assistance
- Investigation memory
"""


from .orchestrator import (
    InvestigationOrchestrator,
)


from .orchestration_schema import (
    InvestigationResult,
)



__all__ = [

    "InvestigationOrchestrator",

    "InvestigationResult",

]