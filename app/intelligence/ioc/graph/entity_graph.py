"""
Sentinel DNA

IOC Entity Graph

Responsible for:
- Creating IOC entities
- Maintaining graph objects
- Preparing relationship analysis
"""

from __future__ import annotations



class EntityGraph:
    """
    IOC entity graph manager.

    Provides:
    - Entity creation
    - Entity storage
    - Entity retrieval
    """


    def __init__(
        self,
    ):
        """
        Initialize in-memory entity graph.
        """

        self.entities = {}



    def create_entity(
        self,
        indicator: dict,
    ) -> dict:
        """
        Create or update an IOC entity.

        Compatible with:
        - Intelligence Fusion Layer
        - IOC Graph API
        """


        entity_id = indicator.get(
            "indicator",
            "unknown",
        )


        entity = {

            "id": entity_id,


            "type": indicator.get(
                "type",
                "unknown",
            ),


            "metadata": {

                "source": "ioc-service",

            },

        }


        self.entities[entity_id] = entity


        return entity



    def get_entity(
        self,
        entity_id: str,
    ) -> dict | None:
        """
        Retrieve an existing IOC entity.
        """


        return self.entities.get(
            entity_id
        )



    def list_entities(
        self,
    ) -> list:
        """
        Return all graph entities.
        """


        return list(
            self.entities.values()
        )