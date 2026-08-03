from datetime import datetime


class ContextEngine:


    def generate(
        self,
        graph
    ):

        return {

            "security_context":
                "Threat relationships analyzed",

            "entities":
                len(graph["nodes"]),

            "relationships":
                len(graph["edges"]),

            "timestamp":
                datetime.utcnow().isoformat()

        }