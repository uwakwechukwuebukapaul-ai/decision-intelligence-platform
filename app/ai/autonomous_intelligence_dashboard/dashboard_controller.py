from datetime import datetime

from .dashboard_state import DashboardState
from .intelligence_aggregator import IntelligenceAggregator
from .health_analyzer import HealthAnalyzer



class DashboardController:


    def __init__(self, user_id):

        self.user_id = user_id



    def generate_dashboard(self):


        dashboard_state = DashboardState(
            self.user_id
        ).generate()



        intelligence = IntelligenceAggregator().aggregate()



        health = HealthAnalyzer().analyze()



        return {


            "user_id":

                self.user_id,



            "dashboard_status":

                "active",



            "dashboard_score":

                99,



            "dashboard_state":

                dashboard_state,



            "intelligence_overview":

                intelligence,



            "system_health":

                health,



            "generated_at":

                datetime.utcnow().isoformat(),



            "version":

                "1.0"

        }