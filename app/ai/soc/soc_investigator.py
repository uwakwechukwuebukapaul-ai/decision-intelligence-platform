from app.ai.soc.threat_analyzer import ThreatAnalyzer
from app.ai.soc.alert_triage_engine import AlertTriageEngine
from app.ai.soc.incident_reasoner import IncidentReasoner
from app.ai.soc.mitre_mapper import MITREMapper
from app.ai.soc.soc_memory import SOCMemory

from datetime import datetime


class SOCInvestigator:


    def __init__(self):

        self.threat = ThreatAnalyzer()

        self.triage = AlertTriageEngine()

        self.reasoner = IncidentReasoner()

        self.mitre = MITREMapper()

        self.memory = SOCMemory()



    def investigate(
        self,
        case
    ):


        evidence = case.get(
            "evidence",
            []
        )


        threat = self.threat.analyze(
            evidence
        )


        alert = self.triage.triage(
            case
        )


        mapping = self.mitre.map_attack(
            evidence
        )


        reasoning = self.reasoner.reason(
            threat
        )


        result = {

            "case":
                case,


            "threat_analysis":
                threat,


            "alert_triage":
                alert,


            "mitre_mapping":
                mapping,


            "reasoning":
                reasoning,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return {

            "status":
                "completed",


            "investigation":
                result

        }