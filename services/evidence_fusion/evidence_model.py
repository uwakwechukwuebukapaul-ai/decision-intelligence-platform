from datetime import datetime
import uuid


class Evidence:
    """
    Unified Sentinel DNA evidence object.

    Normalizes evidence from:
    - Threat intelligence
    - Detection engines
    - Agents
    - Investigations
    """


    def __init__(
        self,
        evidence_type,
        data,
        source
    ):

        self.id = (
            "EVD-"
            + str(uuid.uuid4())[:8]
        )

        self.type = evidence_type

        self.data = data

        self.source = source

        self.timestamp = (
            datetime.utcnow()
            .isoformat()
        )

        self.weight = 0



    def assign_weight(
        self,
        weight
    ):

        self.weight = weight



    def to_dict(self):

        return {

            "id": self.id,

            "type": self.type,

            "data": self.data,

            "source": self.source,

            "weight": self.weight,

            "timestamp": self.timestamp

        }