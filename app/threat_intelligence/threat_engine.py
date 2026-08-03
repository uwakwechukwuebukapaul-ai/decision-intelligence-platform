from datetime import datetime

from .ioc_manager import IOCManager
from .ioc_enricher import IOCEnricher
from .reputation_engine import ReputationEngine
from .campaign_tracker import CampaignTracker
from .threat_actor_tracker import ThreatActorTracker
from .malware_tracker import MalwareTracker
from .intel_memory import IntelMemory
from .intel_logger import IntelLogger


class ThreatIntelligenceEngine:

    def __init__(self):

        self.ioc_manager = IOCManager()
        self.enricher = IOCEnricher()
        self.reputation = ReputationEngine()
        self.campaign = CampaignTracker()
        self.actor = ThreatActorTracker()
        self.malware = MalwareTracker()
        self.memory = IntelMemory()
        self.logger = IntelLogger()


    def analyze(self, threat):

        iocs = self.ioc_manager.extract(threat)

        enrichment = self.enricher.enrich(iocs)

        reputation = self.reputation.check(
            enrichment
        )

        campaign = self.campaign.track(
            threat
        )

        actor = self.actor.identify(
            threat
        )

        malware = self.malware.identify(
            threat
        )

        memory = self.memory.store(
            threat
        )

        log = self.logger.log(
            threat
        )


        return {
            "status": "completed",
            "threat": threat,
            "iocs": iocs,
            "enrichment": enrichment,
            "reputation": reputation,
            "campaign": campaign,
            "threat_actor": actor,
            "malware": malware,
            "memory": memory,
            "log": log,
            "created_at": datetime.utcnow().isoformat()
        }