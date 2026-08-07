"""
Sentinel DNA Learning Engine

Learns new intelligence and stores it in the knowledge base.
"""

from __future__ import annotations

from .knowledge_store import KnowledgeStore


class LearningEngine:
    """
    Learns and persists intelligence knowledge.
    """

    def __init__(self, store: KnowledgeStore):
        self.store = store

    def learn(
        self,
        key: str,
        data: dict,
    ) -> dict:
        """
        Store newly learned intelligence.
        """

        self.store.store(
            key,
            data,
        )

        return {
            "status": "learned",
            "key": key,
            "data": data,
        }