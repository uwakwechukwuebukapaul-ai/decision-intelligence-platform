"""
Agent Metadata

Stores intelligence agent information.
"""


from datetime import UTC, datetime


class AgentMetadata:

    def __init__(
        self,
        name: str,
        version: str,
        capabilities: list[str],
    ):

        self.name = name

        self.version = version

        self.capabilities = capabilities

        self.status = "active"

        self.created_at = (
            datetime.now(UTC)
            .isoformat()
        )


    def deactivate(self):

        self.status = "inactive"


    def activate(self):

        self.status = "active"


    def to_dict(self):

        return {

            "name":
                self.name,

            "version":
                self.version,

            "capabilities":
                self.capabilities,

            "status":
                self.status,

            "created_at":
                self.created_at,

        }