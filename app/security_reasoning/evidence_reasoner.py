from datetime import datetime


class EvidenceReasoner:

    def analyze(self, context):

        return {

            "evidence_sources": [
                "Security Events",
                "Threat Intelligence",
                "Detection Rules",
                "Investigation History"
            ],

            "event":
                context["event"],

            "timestamp":
                datetime.utcnow().isoformat()
        }