"""
Learning Engine

Processes intelligence outcomes
and updates knowledge.
"""


class LearningEngine:

    def __init__(
        self,
        knowledge_store,
    ):

        self.knowledge_store = knowledge_store


    def learn(
        self,
        key: str,
        intelligence: dict,
    ):

        self.knowledge_store.store(
            key,
            intelligence,
        )


        return {
            "status": "learned",
            "key": key,
        }


    def improve(
        self,
        key: str,
        update: dict,
    ):

        existing = (
            self.knowledge_store.retrieve(
                key
            )
            or {}
        )


        existing.update(
            update
        )


        self.knowledge_store.store(
            key,
            existing,
        )


        return existing