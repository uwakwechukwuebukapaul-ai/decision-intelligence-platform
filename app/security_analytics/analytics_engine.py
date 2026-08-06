from datetime import datetime

from .event_analyzer import EventAnalyzer
from .metric_engine import MetricEngine
from .analytics_repository import AnalyticsRepository



class AnalyticsEngine:


    def __init__(self):

        self.event_analyzer = EventAnalyzer()

        self.metric_engine = MetricEngine()

        self.repository = AnalyticsRepository()



    def analyze(self, event):


        analysis = self.event_analyzer.analyze(
            event
        )


        metric = self.metric_engine.calculate(
            analysis
        )


        result = {

            "metric_id":
                self.repository.generate_id(),

            "event_type":
                event.get("type", "security_event"),

            "category":
                "threat_detection",

            "severity":
                metric["severity"],

            "score":
                metric["score"],

            "findings":
                analysis["findings"],

            "created_at":
                datetime.utcnow().isoformat()

        }


        return self.repository.save(result)