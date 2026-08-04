from datetime import datetime

from .evidence_collector import EvidenceCollector
from .evidence_parser import EvidenceParser
from .evidence_classifier import EvidenceClassifier
from .evidence_analyzer import EvidenceAnalyzer
from .evidence_correlator import EvidenceCorrelator
from .evidence_memory import EvidenceMemory
from .evidence_logger import EvidenceLogger



class EvidenceIntelligenceEngine:


    def __init__(self):

        self.collector = EvidenceCollector()
        self.parser = EvidenceParser()
        self.classifier = EvidenceClassifier()
        self.analyzer = EvidenceAnalyzer()
        self.correlator = EvidenceCorrelator()
        self.memory = EvidenceMemory()
        self.logger = EvidenceLogger()



    def analyze(self,event):


        evidence = self.collector.collect(event)


        parsed = self.parser.parse(
            evidence
        )


        classification = self.classifier.classify(
            parsed
        )


        analysis = self.analyzer.analyze(
            parsed
        )


        correlation = self.correlator.correlate(
            analysis
        )


        memory = self.memory.store(
            {
                "evidence": evidence,
                "classification": classification,
                "analysis": analysis
            }
        )


        log = self.logger.log(event)



        return {


            "status":
                "completed",


            "event":
                event,


            "evidence":
                evidence,


            "classification":
                classification,


            "analysis":
                analysis,


            "correlation":
                correlation,


            "memory":
                memory,


            "log":
                log,


            "created_at":
                datetime.utcnow().isoformat()

        }