from datetime import datetime


class RelationshipMapper:


    def map(self, entities):

        return {

            "relationships": [

                "Malware targets Asset",

                "Technique used by Malware",

                "Actor operates Campaign"

            ],

            "entity_count":
                len(
                    entities.get("entities", [])
                ),

            "timestamp":
                datetime.utcnow().isoformat()

        }