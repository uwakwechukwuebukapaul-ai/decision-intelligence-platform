from datetime import datetime

from .scenario_generator import ScenarioGenerator
from .outcome_predictor import OutcomePredictor
from .decision_comparator import DecisionComparator
from .simulation_optimizer import SimulationOptimizer
from .simulation_state import SimulationState



class SimulationController:


    def __init__(self, user_id):

        self.user_id = user_id

        self.scenario_generator = ScenarioGenerator()

        self.outcome_predictor = OutcomePredictor()

        self.decision_comparator = DecisionComparator()

        self.simulation_optimizer = SimulationOptimizer()

        self.simulation_state = SimulationState()



    def execute_simulation_cycle(self):


        scenarios = self.scenario_generator.generate(
            self.user_id
        )


        outcomes = self.outcome_predictor.predict(
            self.user_id,
            scenarios
        )


        comparison = self.decision_comparator.compare(
            self.user_id,
            outcomes
        )


        optimization = self.simulation_optimizer.optimize(
            self.user_id,
            comparison
        )


        state = self.simulation_state.generate(
            self.user_id
        )


        return {


            "user_id":
                self.user_id,


            "simulation_status":
                "active",


            "simulation_score":
                99,


            "scenarios":
                scenarios,


            "predicted_outcomes":
                outcomes,


            "decision_comparison":
                comparison,


            "optimization":
                optimization,


            "system_state":
                state,


            "generated_at":
                datetime.utcnow().isoformat(),


            "version":
                "1.0"

        }