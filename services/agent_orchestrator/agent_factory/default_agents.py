"""
Sentinel DNA Default Agent Registry

Loads the initial autonomous SOC workforce.
"""


from services.specialized_agents import (
    ThreatHunterAgent,
    InvestigationAgent,
    ResponseAgent,
    DetectionEngineerAgent
)



def load_default_agents(
    loader
):

    agents = [

        ThreatHunterAgent,

        InvestigationAgent,

        ResponseAgent,

        DetectionEngineerAgent

    ]


    return loader.load_agents(
        agents
    )