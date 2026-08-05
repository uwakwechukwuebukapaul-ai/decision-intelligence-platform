class InvestigationGateway:

    def investigate(self, case):

        return {
            "case": case,
            "investigation": "started",
            "status": "active"
        }