"""
Sentinel DNA Evidence Intelligence Layer

Responsible for collecting, processing,
classifying, analyzing and correlating
security evidence.
"""

from .evidence_engine import EvidenceIntelligenceEngine

__all__ = [
    "EvidenceIntelligenceEngine"
]