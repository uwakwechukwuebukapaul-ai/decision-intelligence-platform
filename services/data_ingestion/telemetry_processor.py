class TelemetryProcessor:
    """
    Processes security telemetry streams.
    """

    def process(self, telemetry):

        return {
            "telemetry_processed": True,
            "records": len(telemetry)
            if isinstance(telemetry, list)
            else 1
        }