from .graph_node import GraphNode
from .relationship import Relationship


class InvestigationMapper:
    """
    Converts security events into investigation graphs.
    """


    def map_event(
        self,
        event,
        graph
    ):

        incident = GraphNode(
            "incident-001",
            "incident",
            event
        )

        graph.add_node(
            incident
        )


        if "powershell" in event.lower():

            process = GraphNode(
                "process-powershell",
                "process",
                "powershell.exe"
            )

            graph.add_node(
                process
            )


            graph.add_relationship(
                Relationship(
                    "incident-001",
                    "executed",
                    "process-powershell"
                )
            )


        if "ransomware" in event.lower():

            malware = GraphNode(
                "malware-ransomware",
                "malware",
                "ransomware"
            )

            graph.add_node(
                malware
            )


            graph.add_relationship(
                Relationship(
                    "incident-001",
                    "contains",
                    "malware-ransomware"
                )
            )


        return graph