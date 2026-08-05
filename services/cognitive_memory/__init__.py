from .memory_store import MemoryStore
from .investigation_memory import InvestigationMemory
from .threat_memory import ThreatMemory
from .analyst_learning import AnalystLearning
from .memory_retriever import MemoryRetriever
from .pattern_engine import PatternEngine


class CognitiveMemory:

    def __init__(self):
        self.memory_store = MemoryStore()
        self.investigation_memory = InvestigationMemory()
        self.threat_memory = ThreatMemory()
        self.analyst_learning = AnalystLearning()
        self.retriever = MemoryRetriever(self.memory_store)
        self.pattern_engine = PatternEngine()