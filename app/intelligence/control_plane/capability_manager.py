"""
Capability Manager

Maintains available intelligence capabilities.
"""


class CapabilityManager:


    def __init__(self):

        self.capabilities = set()



    def register(
        self,
        capability: str,
    ):

        self.capabilities.add(
            capability
        )



    def available(
        self,
        capability: str,
    ) -> bool:

        return (
            capability
            in self.capabilities
        )



    def list_capabilities(self):

        return list(
            self.capabilities
        )