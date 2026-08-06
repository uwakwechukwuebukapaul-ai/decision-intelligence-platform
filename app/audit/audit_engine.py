from .audit_repository import AuditRepository
from .audit_schema import create_audit_event


class AuditEngine:


    def __init__(self):

        self.repository = AuditRepository()



    def record_event(
        self,
        incident_id,
        event_type,
        action,
        actor="system",
        details=None
    ):

        event = create_audit_event(
            incident_id,
            event_type,
            action,
            actor,
            details
        )

        return self.repository.save(event)



    def record_ai_decision(
        self,
        incident_id,
        decision,
        confidence
    ):

        return self.record_event(
            incident_id,
            "AI_DECISION",
            decision,
            actor="AI_ENGINE",
            details={
                "confidence": confidence
            }
        )



    def record_response_action(
        self,
        incident_id,
        action
    ):

        return self.record_event(
            incident_id,
            "RESPONSE_ACTION",
            action,
            actor="SOAR_ENGINE"
        )



    def get_case_history(
        self,
        incident_id
    ):

        return self.repository.get_by_incident(
            incident_id
        )



    def generate_audit_report(
        self,
        incident_id
    ):

        events = self.get_case_history(
            incident_id
        )

        return {
            "incident_id": incident_id,
            "total_events": len(events),
            "timeline": events,
            "status": "completed"
        }