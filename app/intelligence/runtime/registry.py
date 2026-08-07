"""
Capability Registry

Stores and resolves intelligence capabilities.
"""


class CapabilityRegistry:
    """
    Registry for intelligence handlers.
    """

    def __init__(self):
        self._capabilities = {}


    def register(
        self,
        capability,
        handler,
    ):
        """
        Register intelligence capability.
        """

        self._capabilities[capability] = handler


    def resolve(
        self,
        capability,
    ):
        """
        Retrieve handler.
        """

        return self._capabilities.get(
            capability
        )


    def has(
        self,
        capability,
    ):
        return capability in self._capabilities