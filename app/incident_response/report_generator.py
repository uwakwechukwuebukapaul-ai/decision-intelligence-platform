from datetime import datetime


class ReportGenerator:



    def generate(
        self,
        case,
        evidence,
        timeline
    ):


        return {

            "title":
                "Sentinel DNA Incident Report",

            "case_id":
                case["case_id"],

            "summary":
                "AI generated incident investigation report",

            "evidence_count":
                evidence["count"],

            "timeline_events":
                timeline["event_count"],

            "timestamp":
                datetime.utcnow().isoformat()

        }