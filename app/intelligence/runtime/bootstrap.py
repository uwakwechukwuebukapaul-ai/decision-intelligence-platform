"""
Intelligence Runtime Bootstrap
"""

from .registry import CapabilityRegistry

from .executor import IntelligenceExecutor

from .agent_registry import AgentRegistry

from .default_engines import (
    load_default_engines,
)



def create_intelligence_runtime(
    engines=None,
):

    registry = CapabilityRegistry()


    if engines is None:

        engines = load_default_engines()


    agent_registry = AgentRegistry(
        registry
    )


    agent_registry.register_all(
        engines
    )


    return IntelligenceExecutor(
        registry
    )