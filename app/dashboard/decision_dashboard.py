from app.dashboard.dashboard_memory import (
    DashboardMemory
)

from app.dashboard.decision_visualizer import (
    DecisionVisualizer
)



class DecisionDashboard:



    def __init__(self):

        self.memory = DashboardMemory()

        self.visualizer = DecisionVisualizer()



    def display(
        self,
        decision_result
    ):


        summary = self.visualizer.generate_summary(
            decision_result
        )


        self.memory.store(
            summary
        )


        return {


            "status":
                "dashboard_ready",


            "dashboard":

                {


                    "title":
                        "Autonomous Decision Command Center",


                    "summary":
                        summary

                }

        }



    def history(self):

        return self.memory.get_history()