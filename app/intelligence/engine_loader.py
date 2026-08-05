"""
Engine Loader

Responsible for discovering
and registering intelligence engines.
"""


from app.intelligence.capability_registry import (
    capability_registry
)


from app.intelligence.engine_manifest import (
    EngineManifest
)



class EngineLoader:


    def __init__(self):

        self.loaded_engines = []



    def register_engine(
        self,
        name,
        engine,
        description,
        category
    ):


        manifest = EngineManifest(

            name=name,

            description=description,

            category=category

        )


        capability_registry.register(

            name,

            engine,

            manifest

        )


        self.loaded_engines.append(name)



    def load_core_engines(self):

        """
        Initial engine registration.

        More engines will be migrated here
        gradually.
        """


        return {

            "status":
                "initialized",

            "loaded":
                self.loaded_engines

        }



    def list_loaded_engines(self):

        return self.loaded_engines




engine_loader = EngineLoader()