class DashboardRepository:

    def __init__(self):
        self.dashboards = []

    def save(self, dashboard):
        self.dashboards.append(dashboard)
        return dashboard

    def get_all(self):
        return self.dashboards

    def get_latest(self):
        if not self.dashboards:
            return None

        return self.dashboards[-1]