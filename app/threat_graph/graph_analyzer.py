from datetime import datetime


class GraphAnalyzer:


    def analyze(self, nodes, relationships):

        risk = "low"


        if len(nodes) >= 3:
            risk = "high"


        if len(relationships) >= 3:
            risk = "critical"


        return {

            "node_count": len(nodes),

            "relationship_count":
                len(relationships),

            "risk_level": risk,

            "timestamp":
                datetime.utcnow().isoformat()
        }