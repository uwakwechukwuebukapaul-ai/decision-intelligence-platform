"""
Sentinel DNA - Case Manager

Controls SOC investigation lifecycle.
"""


from __future__ import annotations


import uuid


from .case_schema import InvestigationCase
from .case_store import CaseStore
from .timeline import InvestigationTimeline



class CaseManager:


    def __init__(self):

        self.store = CaseStore()



    def create_case(
        self,
        indicator: str,
        intelligence: dict | None = None,
    ):


        case_id = (
            "INC-"
            +
            uuid.uuid4()
            .hex[:8]
            .upper()
        )


        case = InvestigationCase(

            case_id=case_id,

            indicator=indicator,

            severity=
            intelligence
            .get("risk", {})
            .get("risk", "unknown")
            if intelligence
            else "unknown",

            confidence=
            intelligence
            .get("confidence", 0)
            if intelligence
            else 0,

            evidence=
            intelligence
            or {}

        )


        timeline = InvestigationTimeline()


        timeline.add_event(
            "creation",
            "Investigation case created"
        )


        case.timeline = timeline.get_events()


        self.store.save(
            case
        )


        return case.to_dict()



    def get_case(
        self,
        case_id: str,
    ):

        case = self.store.get(
            case_id
        )


        if case:

            return case.to_dict()


        return None