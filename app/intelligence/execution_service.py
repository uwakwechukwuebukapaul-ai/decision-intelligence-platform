"""
Intelligence Execution Service

Central service layer between API
and Intelligence Fabric.
"""


from app.intelligence.intelligence_fabric import (
    intelligence_fabric
)


from app.intelligence.capability_registry import (
    capability_registry
)



class IntelligenceExecutionService:


    def execute(
        self,
        user_id,
        capability,
        objective=None,
        metadata=None
    ):


        context = (
            intelligence_fabric.create_context(
                user_id=user_id,
                objective=objective,
                metadata=metadata
            )
        )


        if capability not in (
            capability_registry.list_capabilities()
        ):

            raise ValueError(
                f"Capability '{capability}' unavailable"
            )



        result = (
            intelligence_fabric.execute(
                capability,
                context
            )
        )


        return result




intelligence_execution_service = (
    IntelligenceExecutionService()
)