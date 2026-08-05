"""
Sentinel DNA Engine Loader

Responsible for:
- automatic engine discovery
- safe engine initialization
- kernel registration
- engine health tracking
"""


import importlib
import logging


logger = logging.getLogger(__name__)


class EngineLoader:
    """
    Dynamic intelligence engine loader.
    """

    def __init__(self, registry):

        self.registry = registry

        self.loaded_engines = {}

        self.failed_engines = {}



    def load_engine(
        self,
        name,
        module_path,
        class_name
    ):
        """
        Dynamically imports and registers an engine.
        """

        try:

            module = importlib.import_module(
                module_path
            )

            engine_class = getattr(
                module,
                class_name
            )


            engine_instance = engine_class()


            self.registry.register(
                name,
                engine_instance
            )


            self.loaded_engines[name] = {
                "status": "loaded",
                "module": module_path,
                "class": class_name
            }


            return engine_instance


        except Exception as error:

            logger.error(
                f"Failed loading {name}: {error}"
            )


            self.failed_engines[name] = {
                "status": "failed",
                "error": str(error)
            }


            return None



    def load_default_engines(self):
        """
        Loads Sentinel DNA core intelligence engines.
        """

        default_engines = [

            {
                "name": "threat_intelligence",
                "module": "services.threat_intelligence.threat_engine",
                "class": "ThreatEngine"
            },


            {
                "name": "detection_engine",
                "module": "services.detection_engine.detection_engine",
                "class": "DetectionEngine"
            },


            {
                "name": "memory_engine",
                "module": "services.memory_engine.memory_store",
                "class": "MemoryStore"
            },


            {
                "name": "response_engine",
                "module": "services.response_engine.response_engine",
                "class": "ResponseEngine"
            },


            {
                "name": "cyber_twin",
                "module": "services.cyber_twin.cyber_twin_engine",
                "class": "CyberTwinEngine"
            },


            {
                "name": "threat_simulation",
                "module": "services.threat_simulation.attack_simulator",
                "class": "AttackSimulator"
            }

        ]


        results = {}


        for engine in default_engines:

            instance = self.load_engine(
                engine["name"],
                engine["module"],
                engine["class"]
            )


            results[engine["name"]] = (
                "loaded"
                if instance
                else "failed"
            )


        return results



    def status(self):

        return {

            "loaded_engines":
                self.loaded_engines,

            "failed_engines":
                self.failed_engines,

            "total_loaded":
                len(self.loaded_engines),

            "total_failed":
                len(self.failed_engines)

        }