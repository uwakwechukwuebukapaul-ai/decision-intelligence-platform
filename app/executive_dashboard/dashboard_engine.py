from .dashboard_repository import DashboardRepository
from .security_metrics import SecurityMetrics
from .kpi_calculator import KPICalculator
from .dashboard_schema import dashboard_record


class DashboardEngine:

    def __init__(self):
        self.repository = DashboardRepository()
        self.metrics_engine = SecurityMetrics()
        self.kpi_engine = KPICalculator()

    def generate(self, organization, security_data):

        metrics = self.metrics_engine.calculate(security_data)

        score = self.kpi_engine.calculate_score(metrics)

        recommendations = []

        if score["security_level"] == "critical":
            recommendations.extend([
                "Investigate active threats",
                "Improve detection coverage",
                "Reduce exposed assets"
            ])

        elif score["security_level"] == "moderate":
            recommendations.append(
                "Continue security improvement initiatives"
            )

        else:
            recommendations.append(
                "Maintain current security posture"
            )

        dashboard = dashboard_record(
            organization,
            score["security_score"],
            score["security_level"],
            metrics,
            recommendations
        )

        return self.repository.save(dashboard)