import datetime


class InvestigationBuilder:
    """
    Builds unified investigation reports.
    """

    def build(self, intelligence):

        return {

            "investigation_status":
                "completed",

            "intelligence":
                intelligence,

            "created_at":
                datetime.datetime.now(
                    datetime.UTC
                ).isoformat()

        }
