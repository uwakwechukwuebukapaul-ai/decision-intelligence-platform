from datetime import datetime, timezone

from services.observability.service_registry import ServiceRegistry
from services.observability.health_monitor import HealthMonitor
from services.observability.metrics_engine import MetricsEngine
from services.observability.execution_trace import ExecutionTrace


class ObservabilityManager:

    def __init__(self):

        self.registry = ServiceRegistry()
        self.health = HealthMonitor()
        self.metrics = MetricsEngine()
        self.trace = ExecutionTrace()


    def register_service(self, name):

        service = self.registry.register(
            name
        )

        self.health.check(
            name
        )

        return service


    def start_execution(self, name):

        self.metrics.record_execution(
            name
        )

        trace_id = self.trace.start(
            name
        )

        return trace_id


    def complete_execution(
        self,
        name,
        success=True
    ):

        self.metrics.record_result(
            name,
            success
        )

        return self.trace.complete(
            name
        )


    def report(self):

        return {

            "platform":
                "Decision Intelligence Platform",

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),

            "services":
                self.registry.services,

            "health":
                self.health.status(),

            "metrics":
                self.metrics.metrics,

            "trace":
                self.trace.events
        }