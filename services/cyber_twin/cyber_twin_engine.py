from .asset_model import AssetModel
from .environment_graph import EnvironmentGraph
from .risk_projection import RiskProjection
from .security_state import SecurityState



class CyberTwinEngine:
    """
    Main Cyber Twin orchestration engine.

    Provides:
    - environment awareness
    - risk projection
    - security state modeling
    """


    def __init__(self):

        self.assets = AssetModel()

        self.graph = EnvironmentGraph()

        self.risk = RiskProjection()

        self.state = SecurityState()



    def analyze(
        self,
        environment
    ):

        assets = environment.get(
            "assets",
            []
        )

        threats = environment.get(
            "threats",
            []
        )

        vulnerabilities = environment.get(
            "vulnerabilities",
            []
        )


        return {

            "status": "cyber_twin_analysis_completed",

            "asset_inventory":

                self.assets.inventory(
                    assets
                ),

            "environment_graph":

                self.graph.build(
                    assets
                ),

            "risk_projection":

                self.risk.calculate(

                    threats,

                    vulnerabilities

                ),

            "security_state":

                self.state.update(

                    assets,

                    threats

                )

        }