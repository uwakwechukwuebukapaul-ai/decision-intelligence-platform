from .intelligence_context import IntelligenceContext
from .intelligence_registry import registry



class IntelligenceFabric:
    """
    Central orchestration layer.

    Controls:
    - context creation
    - capability selection
    - execution
    - intelligence response
    """


    def create_context(
        self,
        user_id,
        objective=None,
        metadata=None
    ):

        return IntelligenceContext(
            user_id=user_id,
            objective=objective,
            metadata=metadata
        )


    def execute(
        self,
        capability,
        context,
        **kwargs
    ):

        result = registry.execute(
            capability,
            context,
            **kwargs
        )


        context.add_history(
            {
                "capability": capability,
                "result": result
            }
        )


        return {
            "status": "success",
            "capability": capability,
            "context": context.to_dict(),
            "result": result
        }



intelligence_fabric = IntelligenceFabric()