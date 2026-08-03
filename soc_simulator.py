from app.ai.simulation.scenario_engine import ScenarioEngine
from app.ai.simulation.roi_simulator import ROISimulator
from app.ai.simulation.impact_analyzer import ImpactAnalyzer
from app.ai.simulation.simulation_memory import SimulationMemory

from datetime import datetime


class SOCSimulator:


    def __init__(self):

        self.scenario = ScenarioEngine()

        self.roi = ROISimulator()

        self.impact = ImpactAnalyzer()

        self.memory = SimulationMemory()



    def simulate(
        self,
        model
    ):


        scenario = self.scenario.create_scenario(
            model
        )


        roi = self.roi.calculate(
            scenario
        )


        impact = self.impact.analyze(
            scenario,
            roi
        )


        result = {

            "scenario":
                scenario,


            "roi":
                roi,


            "impact":
                impact,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return {

            "status":
                "completed",


            "simulation":
                result

        }