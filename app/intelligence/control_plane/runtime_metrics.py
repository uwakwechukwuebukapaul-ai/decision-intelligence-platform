"""
Runtime Metrics

Control plane operational metrics.
"""


class RuntimeMetrics:
    """
    Provides runtime statistics.
    """

    def __init__(self):
        self.metrics = {
            "tasks_processed": 0,
            "active_agents": 0,
            "failed_tasks": 0,
        }

    def increment(
        self,
        metric: str,
    ):
        if metric in self.metrics:
            self.metrics[metric] += 1

    def get_metrics(self) -> dict:
        return {
            "component": "intelligence_control_plane",
            "metrics": self.metrics,
        }