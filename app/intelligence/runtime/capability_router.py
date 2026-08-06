"""
Capability Router

Maps intelligence capabilities
to execution handlers.
"""


class CapabilityRouter:

    def __init__(self):

        self.handlers = {}

    def register(
        self,
        capability: str,
        handler,
    ):

        self.handlers[capability] = handler

    def resolve(
        self,
        capability: str,
    ):

        return self.handlers.get(
            capability
        )

    def available_capabilities(self):

        return list(
            self.handlers.keys()
        )