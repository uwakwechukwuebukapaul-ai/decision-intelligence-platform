from datetime import datetime

from .ioc_manager import IOCManager
from .feed_connector import FeedConnector
from .threat_actor_tracker import ThreatActorTracker
from .malware_intelligence import MalwareIntelligence
from .campaign_tracker import CampaignTracker
from .intel_memory import IntelMemory
from .intel_logger import IntelLogger


class ThreatIntelligenceEngine:

    def __init__(self):

        self.ioc = IOCManager()
        self.feed = FeedConnector()
        self.actor = ThreatActorTracker()
        self.malware = MalwareIntelligence()
        self.campaign = CampaignTracker()

        self.memory = IntelMemory()
        self.logger = IntelLogger()


    def analyze(self, event):

        iocs = self.ioc.extract(event)

        feeds = self.feed.enrich(event)

        actors = self.actor.track(event)

        malware = self.malware.analyze(event)

        campaigns = self.campaign.identify(event)


        memory = self.memory.store(
            event,
            {
                "IOCs": iocs,
                "Actors": actors,
                "Malware": malware,
                "Campaigns": campaigns
            }
        )


        log = self.logger.log(event)


        return {

            "status": "completed",

            "event": event,

            "ioc_analysis": iocs,

            "threat_feeds": feeds,

            "threat_actor": actors,

            "malware": malware,

            "campaign": campaigns,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }