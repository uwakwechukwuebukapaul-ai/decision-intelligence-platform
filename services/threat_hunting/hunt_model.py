from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class HuntModel:
    """
    Threat hunting operation model.

    Represents:
    - hunting hypothesis
    - generated query
    - findings
    - execution state
    """

    hypothesis: str

    query: str

    findings: List[Dict] = field(
        default_factory=list
    )

    status: str = "created"


    def to_dict(self):

        return {

            "hypothesis":
                self.hypothesis,

            "query":
                self.query,

            "findings":
                self.findings,

            "status":
                self.status

        }