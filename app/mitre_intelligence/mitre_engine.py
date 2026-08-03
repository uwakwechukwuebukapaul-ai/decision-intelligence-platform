from datetime import datetime

from .technique_mapper import TechniqueMapper
from .tactic_mapper import TacticMapper
from .attack_chain_builder import AttackChainBuilder
from .coverage_analyzer import CoverageAnalyzer
from .detection_mapper import DetectionMapper
from .mitre_memory import MITREMemory
from .mitre_logger import MITRELogger



class MITREIntelligenceEngine:


    def __init__(self):

        self.techniques = TechniqueMapper()

        self.tactics = TacticMapper()

        self.attack_chain = AttackChainBuilder()

        self.coverage = CoverageAnalyzer()

        self.detection = DetectionMapper()

        self.memory = MITREMemory()

        self.logger = MITRELogger()



    def analyze(self, event):


        techniques = self.techniques.map(
            event
        )


        tactics = self.tactics.map(
            event
        )


        chain = self.attack_chain.build(
            event
        )


        coverage = self.coverage.analyze(
            techniques
        )


        detections = self.detection.map(
            techniques
        )


        memory = self.memory.store(
            event
        )


        log = self.logger.log(
            event
        )


        return {


            "status":

                "completed",


            "event":

                event,


            "techniques":

                techniques,


            "tactics":

                tactics,


            "attack_chain":

                chain,


            "coverage":

                coverage,


            "detections":

                detections,


            "memory":

                memory,


            "log":

                log,


            "created_at":

                datetime.utcnow().isoformat()

        }