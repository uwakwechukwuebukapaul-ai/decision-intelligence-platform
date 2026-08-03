from datetime import datetime

from .rule_generator import RuleGenerator
from .sigma_generator import SigmaGenerator
from .kql_generator import KQLGenerator
from .spl_generator import SPLGenerator
from .coverage_analyzer import CoverageAnalyzer
from .false_positive_analyzer import FalsePositiveAnalyzer
from .mitre_detector_mapper import MITREDetectorMapper
from .detection_memory import DetectionMemory
from .detection_logger import DetectionLogger



class AIDetectionEngine:


    def __init__(self):

        self.rule_generator = RuleGenerator()
        self.sigma_generator = SigmaGenerator()
        self.kql_generator = KQLGenerator()
        self.spl_generator = SPLGenerator()

        self.coverage_analyzer = CoverageAnalyzer()
        self.false_positive_analyzer = FalsePositiveAnalyzer()

        self.mitre_mapper = MITREDetectorMapper()

        self.memory = DetectionMemory()
        self.logger = DetectionLogger()



    def generate(self, threat):

        return {

            "status":
                "completed",

            "threat":
                threat,


            "rule":
                self.rule_generator.generate(
                    threat
                ),


            "sigma":
                self.sigma_generator.generate(
                    threat
                ),


            "kql":
                self.kql_generator.generate(
                    threat
                ),


            "spl":
                self.spl_generator.generate(
                    threat
                ),


            "coverage":
                self.coverage_analyzer.analyze(
                    threat
                ),


            "false_positive":
                self.false_positive_analyzer.analyze(
                    threat
                ),


            "mitre":
                self.mitre_mapper.map(
                    threat
                ),


            "memory":
                self.memory.store(
                    threat
                ),


            "log":
                self.logger.log(
                    threat
                ),


            "created_at":
                datetime.utcnow().isoformat()
        }