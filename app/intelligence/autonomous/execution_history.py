"""
Sentinel DNA - Autonomous Execution History

Tracks autonomous agent execution events.

Responsibilities:

- Store execution records
- Track agent actions
- Preserve investigation history
- Support audit trails
- Provide future persistence layer integration
"""


from __future__ import annotations


from datetime import datetime
from uuid import uuid4





class ExecutionHistory:
    """
    Autonomous execution audit history manager.
    """



    def __init__(self):

        self.records = []



    def record(
        self,
        *,
        agent: str,
        action: str,
        status: str,
        result: dict | None = None,
    ) -> dict:
        """
        Store execution event.
        """

        entry = {

            "execution_id": f"EXEC-{uuid4().hex[:8]}",

            "agent": agent,

            "action": action,

            "status": status,

            "result": result or {},

            "created_at": datetime.utcnow().isoformat(),

        }


        self.records.append(entry)


        return entry





    def list_history(self) -> list:
        """
        Return execution history.
        """

        return self.records





    def latest(
        self,
    ) -> dict | None:
        """
        Return latest execution.
        """

        if not self.records:

            return None


        return self.records[-1]





    def clear(self) -> None:
        """
        Clear runtime history.
        """

        self.records = []