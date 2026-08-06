"""
Sentinel DNA

IOC Case Repository

Temporary persistence abstraction.

Designed to later connect:
- SQLAlchemy
- PostgreSQL
- Case Management Engine
"""


from __future__ import annotations

import uuid
from datetime import datetime



class IOCCaseRepository:
    """
    IOC investigation case storage.
    """


    def __init__(self):

        self.cases = {}



    def create_case(
        self,
        case_data: dict,
    ) -> dict:
        """
        Create investigation case.
        """


        case_id = (
            "IOC-"
            + datetime.utcnow()
            .strftime("%Y%m%d")
            + "-"
            + uuid.uuid4()
            .hex[:6]
            .upper()
        )


        case = {

            "case_id": case_id,

            "status": "open",

            "created_at": datetime.utcnow()
            .isoformat(),

            **case_data,

        }


        self.cases[case_id] = case


        return case



    def get_case(
        self,
        case_id: str,
    ) -> dict | None:

        return self.cases.get(
            case_id
        )