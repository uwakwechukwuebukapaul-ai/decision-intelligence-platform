"""
Intelligence Controller

Main control interface for autonomous execution.
"""


class IntelligenceController:


    def __init__(
        self,
        task_manager,
        policy_engine,
        capability_manager,
        audit_logger,
    ):

        self.task_manager = task_manager

        self.policy_engine = policy_engine

        self.capability_manager = capability_manager

        self.audit_logger = audit_logger



    def submit(
        self,
        capability: str,
        payload: dict,
    ):

        if not self.capability_manager.available(
            capability
        ):

            raise ValueError(
                "Capability unavailable"
            )



        if not self.policy_engine.check(
            capability
        ):

            raise PermissionError(
                "Capability blocked by policy"
            )



        task = self.task_manager.create_task(
            capability,
            payload,
        )


        self.audit_logger.record(
            "task_created",
            {
                "task_id": task.task_id,
                "capability": capability,
            }
        )


        return task



    def get_status(self):
        """
        Return control plane operational status.

        Used by monitoring APIs and health dashboards.
        """

        return {
            "component": "intelligence_control_plane",
            "status": "operational",
            "task_manager": "available",
            "policy_engine": "available",
            "capability_manager": "available",
            "audit_logger": "available",
        }