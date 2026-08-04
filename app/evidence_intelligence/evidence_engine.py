from datetime import datetime

from .evidence_collector import EvidenceCollector
from .evidence_parser import EvidenceParser
from .evidence_classifier import EvidenceClassifier
from .evidence_analyzer import EvidenceAnalyzer
from .evidence_correlator import EvidenceCorrelator
from .evidence_memory import EvidenceMemory
from .evidence_logger import EvidenceLogger


class EvidenceIntelligenceEngine:
    """
    Sentinel DNA Evidence Intelligence Engine

    Responsible for:
    - Evidence collection
    - Evidence parsing
    - Evidence classification
    - Evidence analysis
    - Evidence correlation
    - Evidence memory
    - Evidence auditing
    """

    def __init__(self):

        self.collector = EvidenceCollector()
        self.parser = EvidenceParser()
        self.classifier = EvidenceClassifier()
        self.analyzer = EvidenceAnalyzer()
        self.correlator = EvidenceCorrelator()
        self.memory = EvidenceMemory()
        self.logger = EvidenceLogger()


    def analyze(self, event):

        # Collect evidence
        evidence = self.collector.collect(
            event
        )


        # Parse evidence artifacts
        parsed = self.parser.parse(
            evidence
        )


        # Classify evidence severity
        classification = self.classifier.classify(
            parsed
        )


        # Analyze security findings
        analysis = self.analyzer.analyze(
            parsed
        )


        # Correlate with security intelligence
        correlation = self.correlator.correlate(
            analysis
        )


        # Store intelligence memory
        memory = self.memory.store(
            {
                "event": event,
                "evidence": evidence,
                "classification": classification,
                "analysis": analysis,
                "correlation": correlation
            }
        )


        # Generate audit log
        log = self.logger.log(
            event
        )


        return {

            "status": "completed",

            "event": event,


            "evidence": evidence,


            "parsed_evidence": parsed,


            "classification": classification,


            "analysis": analysis,


            "correlation": correlation,


            "memory": memory,


            "log": log,


            "created_at":
                datetime.utcnow().isoformat()

        }