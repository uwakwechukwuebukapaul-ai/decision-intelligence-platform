from app.database.db import SessionLocal
from app.models.knowledge_node import KnowledgeNode
from app.models.knowledge_relationship import KnowledgeRelationship


class KnowledgeRepository:


    def save_node(
        self,
        node_id,
        node_type,
        name,
        data=""
    ):

        db = SessionLocal()

        node = KnowledgeNode(
            node_id=node_id,
            node_type=node_type,
            name=name,
            data=data
        )

        db.add(node)
        db.commit()
        db.refresh(node)

        result = {
            "node_id": node.node_id,
            "node_type": node.node_type,
            "name": node.name,
            "status": "stored"
        }

        db.close()

        return result



    def search(
        self,
        keyword
    ):

        db = SessionLocal()

        nodes = (
            db.query(KnowledgeNode)
            .filter(
                KnowledgeNode.name.contains(keyword)
            )
            .all()
        )


        results = [
            {
                "node_id": node.node_id,
                "type": node.node_type,
                "name": node.name
            }

            for node in nodes
        ]


        db.close()


        return {
            "count": len(results),
            "results": results
        }



    def save_relationship(
        self,
        relationship_id,
        source,
        target,
        relation
    ):

        db = SessionLocal()


        relationship = KnowledgeRelationship(
            relationship_id=relationship_id,
            source=source,
            target=target,
            relation=relation
        )


        db.add(relationship)

        db.commit()

        result = {

            "relationship_id": relationship.relationship_id,

            "status": "stored"

        }


        db.close()


        return result