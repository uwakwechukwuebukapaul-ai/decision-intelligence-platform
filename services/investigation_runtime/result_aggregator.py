import datetime


class ResultAggregator:

    def aggregate(
        self,
        context,
        investigation,
        engines
    ):

        return {
            "investigation_id": context["context_id"],
            "event": context["event"],
            "investigation": investigation,
            "engine_results": engines,
            "final_status": "completed",
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
