"""
Sentinel DNA Knowledge Graph Engine

Provides:
- Entity representation
- Relationship intelligence
- Attack path discovery
- Investigation reasoning
"""

from .entity import Entity
from .knowledge_graph import KnowledgeGraph
from .relationship_engine import RelationshipEngine
from .attack_path import AttackPathEngine


# Backward compatibility
KnowledgeGraphEngine = KnowledgeGraph


__all__ = [
    "Entity",
    "KnowledgeGraph",
    "KnowledgeGraphEngine",
    "RelationshipEngine",
    "AttackPathEngine"
]