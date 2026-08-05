from .threat_hunter import ThreatHunter
from .hunt_planner import HuntPlanner
from .query_generator import QueryGenerator
from .behavior_detector import BehaviorDetector
from .anomaly_engine import AnomalyEngine
from .attack_surface_mapper import AttackSurfaceMapper
from .hunt_memory import HuntMemory
from .threat_hunting_orchestrator import ThreatHuntingOrchestrator


class AutonomousThreatHuntingEngine:
    """
    Sentinel DNA Autonomous Threat Hunting Engine.

    Provides:
    - AI threat hunting
    - hypothesis generation
    - anomaly discovery
    - attack surface analysis
    - continuous hunting memory
    """

    def __init__(self):

        self.hunter = ThreatHunter()
        self.planner = HuntPlanner()
        self.query_generator = QueryGenerator()
        self.behavior_detector = BehaviorDetector()
        self.anomaly_engine = AnomalyEngine()
        self.attack_surface_mapper = AttackSurfaceMapper()
        self.memory = HuntMemory()
        self.orchestrator = ThreatHuntingOrchestrator()


    def status(self):

        return {
            "engine": "Autonomous Threat Hunting Engine",
            "status": "operational"
        }