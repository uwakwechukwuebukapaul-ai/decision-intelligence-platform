from datetime import datetime


class ThreatVisualizer:


    def visualize(self, incident):

        return {

            "graph_type":

                "Threat Relationship Graph",

            "nodes":

            [

                "Threat Actor",

                "Malware",

                "Technique",

                "Target Asset"

            ],

            "incident":

                incident,

            "timestamp":

                datetime.utcnow().isoformat()

        }