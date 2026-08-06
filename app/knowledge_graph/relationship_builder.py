from datetime import datetime


class RelationshipBuilder:


    def build(
        self,
        source,
        target,
        relationship
    ):


        return {

            "source":
            source,


            "target":
            target,


            "relationship":
            relationship,


            "confidence":
            0.9,


            "created_at":
            datetime.utcnow().isoformat()

        }