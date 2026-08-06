from .intelligence_engine import IntelligenceEngine


# Backward compatibility layer
IntelligenceManager = IntelligenceEngine


__all__ = [
    "IntelligenceEngine",
    "IntelligenceManager",
]