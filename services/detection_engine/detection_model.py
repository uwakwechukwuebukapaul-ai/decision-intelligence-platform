from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class DetectionModel:
    """
    Detection output contract.

    Represents a generated security detection.
    """


    name: str

    severity: str

    description: str


    logic: List[str] = field(
        default_factory=list
    )


    mitre: List[str] = field(
        default_factory=list
    )


    metadata: Dict = field(
        default_factory=dict
    )


    def to_dict(self):

        return {

            "name":
                self.name,

            "severity":
                self.severity,

            "description":
                self.description,

            "logic":
                self.logic,

            "mitre":
                self.mitre,

            "metadata":
                self.metadata

        }