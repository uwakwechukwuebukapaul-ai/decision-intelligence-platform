from datetime import datetime


from .ioc_manager import IOCManager
from .threat_feed_engine import ThreatFeedEngine
from .reputation_engine import ReputationEngine
from .actor_tracker import ActorTracker
from .campaign_tracker import CampaignTracker
from .threat_graph import ThreatGraph
from .intel_memory import IntelMemory



class IntelligenceEngine:
    """
    Sentinel DNA Threat Intelligence Operating System.
    """


    def __init__(self):

        self.ioc = IOCManager()

        self.feeds = ThreatFeedEngine()

        self.reputation = ReputationEngine()

        self.actor = ActorTracker()

        self.campaign = CampaignTracker()

        self.graph = ThreatGraph()

        self.memory = IntelMemory()



    def analyze(
        self,
        event
    ):


        feed = self.feeds.collect(
            "Sentinel DNA Intelligence Feed"
        )


        reputation = self.reputation.analyze(
            event
        )


        actor = self.actor.identify(
            event
        )


        campaign = self.campaign.track(
            event
        )


        graph = self.graph.build(
            event,
            actor["actors"]
        )


        result = {


            "status":
                "completed",


            "event":
                event,


            "feed":
                feed,


            "reputation":
                reputation,


            "actor":
                actor,


            "campaign":
                campaign,


            "threat_graph":
                graph,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return result