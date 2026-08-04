from datetime import datetime


class EngineCoordinator:


    def coordinate(self,event):

        return {

            "connected_engines":[

                "Evidence Intelligence",

                "Threat Hunting",

                "Knowledge Graph",

                "Cognitive Core",

                "Intelligence Fusion",

                "SOAR"

            ],

            "event":event,

            "status":"coordinated",

            "timestamp":
                datetime.utcnow().isoformat()

        }