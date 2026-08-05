"""
Capability Registry

Central storage for intelligence
capabilities available to the platform.
"""


class CapabilityRegistry:


    def __init__(self):

        self.capabilities = {}



    def register(
        self,
        name,
        engine,
        manifest=None
    ):

        self.capabilities[name] = {

            "engine": engine,

            "manifest": manifest

        }



    def unregister(
        self,
        name
    ):

        if name in self.capabilities:

            del self.capabilities[name]



    def get(
        self,
        name
    ):

        capability = self.capabilities.get(name)

        if capability:

            return capability["engine"]

        return None



    def get_manifest(
        self,
        name
    ):

        capability = self.capabilities.get(name)

        if capability:

            return capability["manifest"]


        return None



    def list_capabilities(self):

        return list(
            self.capabilities.keys()
        )



    def execute(
        self,
        name,
        *args,
        **kwargs
    ):


        engine = self.get(name)


        if not engine:

            raise ValueError(
                f"Capability '{name}' is not registered"
            )


        return engine(
            *args,
            **kwargs
        )




# Global Registry Instance

capability_registry = CapabilityRegistry()