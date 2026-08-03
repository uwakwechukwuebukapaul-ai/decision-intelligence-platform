from datetime import datetime

from .ioc_manager import IOCManager
from .ioc_enrichment import IOCEnrichment
from .reputation_engine import ReputationEngine
from .feed_connector import FeedConnector
from .threat_actor_tracker import ThreatActorTracker
from .malware_intelligence import MalwareIntelligence
from .indicator_database import IndicatorDatabase
from .threat_memory import ThreatMemory
from .threat_logger import ThreatLogger


class ThreatIntelligenceEngine:


    def __init__(self):

        self.ioc = IOCManager()
        self.enrichment = IOCEnrichment()
        self.reputation = ReputationEngine()
        self.feeds = FeedConnector()
        self.actor = ThreatActorTracker()
        self.malware = MalwareIntelligence()
        self.database = IndicatorDatabase()
        self.memory = ThreatMemory()
        self.logger = ThreatLogger()


    def analyze(self, event):

        ioc_result = self.ioc.extract(event)

        enrichment_result = self.enrichment.enrich(
            ioc_result
        )

        reputation_result = self.reputation.score(
            ioc_result
        )

        feed_result = self.feeds.lookup(
            event
        )

        actor_result = self.actor.analyze(
            event
        )

        malware_result = self.malware.analyze(
            event
        )

        database_result = self.database.store(
            ioc_result
        )

        memory_result = self.memory.store(
            event
        )

        log_result = self.logger.record(
            event
        )


        return {

            "status": "completed",

            "event": event,

            "ioc_analysis": ioc_result,

            "enrichment": enrichment_result,

            "reputation": reputation_result,

            "feeds": feed_result,

            "threat_actor": actor_result,

            "malware": malware_result,

            "indicator_database": database_result,

            "memory": memory_result,

            "log": log_result,

            "created_at":
                datetime.utcnow().isoformat()

        }