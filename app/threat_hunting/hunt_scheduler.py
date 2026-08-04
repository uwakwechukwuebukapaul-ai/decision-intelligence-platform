from datetime import datetime


class HuntScheduler:

    def create(self, hypothesis):

        return {
            "schedule": "Immediate",
            "priority": "critical",
            "hypothesis": hypothesis["hypothesis"],
            "timestamp": datetime.now().isoformat()
        }