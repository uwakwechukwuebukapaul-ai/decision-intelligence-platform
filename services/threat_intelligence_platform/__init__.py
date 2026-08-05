from .threat_intelligence_engine import ThreatIntelligenceEngine
from .ioc_enrichment import IOCEnrichment
from .threat_actor_intelligence import ThreatActorIntelligence
from .malware_intelligence import MalwareIntelligence
from .vulnerability_intelligence import VulnerabilityIntelligence
from .campaign_tracker import CampaignTracker
from .intelligence_collector import IntelligenceCollector
from .threat_intelligence_orchestrator import ThreatIntelligenceOrchestrator


class ThreatIntelligencePlatform:
    """
    Enterprise Threat Intelligence Platform.

    Coordinates:
    - IOC enrichment
    - Threat actor tracking
    - Malware intelligence
    - Vulnerability intelligence
    - Campaign tracking
    - Intelligence collection
    """

    def __init__(self):
        self.engine = ThreatIntelligenceEngine()
        self.ioc = IOCEnrichment()
        self.actors = ThreatActorIntelligence()
        self.malware = MalwareIntelligence()
        self.vulnerabilities = VulnerabilityIntelligence()
        self.campaigns = CampaignTracker()
        self.collector = IntelligenceCollector()
        self.orchestrator = ThreatIntelligenceOrchestrator()

    def status(self):
        return {
            "platform": "Threat Intelligence Platform",
            "status": "operational",
            "modules": [
                "ioc_enrichment",
                "threat_actor_intelligence",
                "malware_intelligence",
                "vulnerability_intelligence",
                "campaign_tracker",
                "intelligence_collector"
            ]
        }