"""
Sentinel DNA

IOC Relationship Engine

Determines relationships between
security entities.
"""


from __future__ import annotations



class RelationshipEngine:
    """
    Creates intelligence relationships.
    """



    def analyze(
        self,
        source: dict,
        target: dict,
    ) -> dict:
        """
        Determine relationship type.
        """


        source_type = source.get(
            "type"
        )

        target_type = target.get(
            "type"
        )


        relationship = "associated_with"


        if (
            source_type == "domain"
            and target_type == "ip"
        ):

            relationship = "resolves_to"



        elif (
            source_type == "hash"
            and target_type == "malware"
        ):

            relationship = "sample_of"



        elif (
            source_type == "ip"
            and target_type == "domain"
        ):

            relationship = "hosts"



        return {

            "source": source.get(
                "id"
            ),

            "target": target.get(
                "id"
            ),

            "relationship": relationship,

        }