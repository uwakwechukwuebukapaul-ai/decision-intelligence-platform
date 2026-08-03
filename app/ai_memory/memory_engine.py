from datetime import datetime

from .memory_store import MemoryStore
from .incident_memory import IncidentMemory
from .threat_memory import ThreatMemory
from .investigation_memory import InvestigationMemory
from .response_memory import ResponseMemory
from .analyst_memory import AnalystMemory
from .pattern_recognition import PatternRecognition


class AIMemoryEngine:

    def __init__(self):

        self.store = MemoryStore()

        self.incident = IncidentMemory()
        self.threat = ThreatMemory()
        self.investigation = InvestigationMemory()
        self.response = ResponseMemory()
        self.analyst = AnalystMemory()
        self.pattern = PatternRecognition()


    def learn(self, event):

        incident = self.incident.remember(event)

        threat = self.threat.remember(event)

        investigation = self.investigation.store_investigation(event)

        response = self.response.remember_response(event)

        analyst = self.analyst.record(
            "AI automated analysis"
        )

        patterns = self.pattern.analyze(event)


        memories = [
            incident,
            threat,
            investigation,
            response,
            analyst,
            {
                "type": "pattern",
                "data": patterns
            }
        ]


        stored = []


        for memory in memories:

            stored.append(
                self.store.store(
                    memory["category"] if "category" in memory else memory["type"],
                    memory
                )
            )


        return {
            "status": "completed",
            "event": event,
            "memories_created": len(stored),
            "patterns": patterns,
            "memory_records": stored,
            "created_at": datetime.utcnow().isoformat()
        }