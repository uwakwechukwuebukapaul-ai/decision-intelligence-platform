"""
Sentinel DNA Intelligence Fusion Service
"""

from .fusion_engine import FusionEngine


class IntelligenceFusionEngine:

    def __init__(self):

        self.engine = FusionEngine()


    def analyze(self, incident_id: str):

        return self.engine.analyze(
            incident_id
        )