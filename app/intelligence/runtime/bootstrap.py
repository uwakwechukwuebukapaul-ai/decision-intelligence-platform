"""
Intelligence Runtime Bootstrap

Creates production intelligence runtime.
"""

from .registry import CapabilityRegistry

from .executor import IntelligenceExecutor

from .agent_registry import AgentRegistry



def create_intelligence_runtime(
    engines=None,
):
    """
    Creates configured intelligence executor.
    """

    registry = CapabilityRegistry()


    if engines:

        agent_registry = AgentRegistry(
            registry
        )

        agent_registry.register_all(
            engines
        )


    executor = IntelligenceExecutor(
        registry
    )


    return executor