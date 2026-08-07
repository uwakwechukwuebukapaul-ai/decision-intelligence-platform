"""
Sentinel DNA Agent Registry

Central registry for AI SOC agents.
"""

from __future__ import annotations

import logging


logger = logging.getLogger(__name__)


class AgentRegistry:

    def __init__(self):

        self.agents = {}


    def register(
        self,
        agent
    ):

        name = agent.__class__.__name__

        self.agents[name] = agent

        logger.info(
            "Registered AI agent: %s",
            name
        )


    def get(
        self,
        name
    ):

        return self.agents.get(
            name
        )


    def run_agent(
        self,
        name,
        investigation
    ):

        agent = self.get(name)


        if not agent:

            raise ValueError(
                f"Agent {name} not found"
            )


        return agent.analyze(
            investigation
        )


    def list_agents(
        self
    ):

        return list(
            self.agents.keys()
        )