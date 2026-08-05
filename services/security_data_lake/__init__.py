from .data_store import DataStore
from .event_repository import EventRepository
from .evidence_repository import EvidenceRepository
from .investigation_history import InvestigationHistory
from .search_engine import SearchEngine
from .retention_manager import RetentionManager
from .data_lifecycle import DataLifecycle


class SecurityDataLake:

    def __init__(self):

        self.store = DataStore()
        self.events = EventRepository()
        self.evidence = EvidenceRepository()
        self.history = InvestigationHistory()
        self.search = SearchEngine()
        self.retention = RetentionManager()
        self.lifecycle = DataLifecycle()


    def ingest(self, data):

        return self.store.save(data)


    def status(self):

        return {
            "service": "Security Data Lake",
            "status": "ready",
            "components": [
                "data_store",
                "event_repository",
                "evidence_repository",
                "investigation_history",
                "search_engine",
                "retention_manager",
                "data_lifecycle"
            ]
        }