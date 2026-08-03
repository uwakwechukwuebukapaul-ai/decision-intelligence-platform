"""
Mission Execution Engine v50

Responsible for:
- Executing assigned missions
- Routing missions to agents
- Tracking execution results
- Updating mission lifecycle
"""


from datetime import datetime



class ExecutionEngine:


    def __init__(
        self,
        mission_manager,
        agent_manager
    ):

        self.mission_manager = mission_manager

        self.agent_manager = agent_manager



    # =====================================
    # Execute Mission
    # =====================================

    def execute_mission(
        self,
        mission_id
    ):


        missions = (
            self.mission_manager.list_missions()
        )


        mission = None


        for item in missions:

            if item["mission_id"] == mission_id:

                mission = item

                break



        if not mission:

            return {

                "error":
                    "Mission not found"

            }



        agent = self._select_agent(
            mission
        )



        if not agent:

            return {

                "error":
                    "No suitable agent available"

            }



        mission = (
            self.mission_manager.assign_mission(
                mission_id,
                agent["agent_id"]
            )
        )


        self.mission_manager.start_mission(
            mission_id
        )



        result = self._run_agent(
            agent,
            mission
        )



        self.mission_manager.complete_mission(
            mission_id
        )



        return {

            "mission_id":
                mission_id,


            "agent":
                agent["name"],


            "result":
                result,


            "status":
                "completed",


            "completed_at":
                datetime.utcnow().isoformat()

        }



    # =====================================
    # Agent Selection Logic
    # =====================================

    def _select_agent(
        self,
        mission
    ):


        agents = (
            self.agent_manager.list_agents()
        )


        title = (
            mission["title"]
            .lower()
        )


        for agent in agents:


            capabilities = [
                item.lower()
                for item in agent.get(
                    "capabilities",
                    []
                )
            ]



            if (
                "research" in title
                and
                "information_analysis" in capabilities
            ):

                return agent



            if (
                "forecast" in title
                and
                "forecasting" in capabilities
            ):

                return agent



            if (
                "decision" in title
                and
                "decision_analysis" in capabilities
            ):

                return agent



        # fallback agent

        if agents:

            return agents[0]


        return None



    # =====================================
    # Agent Execution Simulation
    # =====================================

    def _run_agent(
        self,
        agent,
        mission
    ):


        return {

            "agent":
                agent["name"],


            "analysis":
                (
                    f"{agent['name']} "
                    f"processed mission: "
                    f"{mission['objective']}"
                ),


            "insights":[

                "Pattern analysis completed",

                "Strategic evaluation generated",

                "Recommendation pipeline executed"

            ]

        }