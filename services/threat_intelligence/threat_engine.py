from .indicator_matcher import IndicatorMatcher
from .reputation_engine import ReputationEngine
from .intelligence_feed import IntelligenceFeed
from .correlation_engine import CorrelationEngine
from .threat_logger import ThreatLogger


class ThreatIntelligenceEngine:

    def __init__(self):

        self.matcher = IndicatorMatcher()
        self.reputation = ReputationEngine()
        self.feed = IntelligenceFeed()
        self.correlation = CorrelationEngine()
        self.logger = ThreatLogger()


    def analyze(self, event):

        indicators = self.matcher.match(event)

        reputation = self.reputation.evaluate(
            indicators
        )

        feed_data = self.feed.collect(event)

        correlation = self.correlation.correlate(
            indicators
        )

        result = {

            "event": event,

            "indicators": indicators,

            "reputation": reputation,

            "feed": feed_data,

            "correlation": correlation,

            "status": "threat_intelligence_processed"

        }

        self.logger.log(result)

        return result