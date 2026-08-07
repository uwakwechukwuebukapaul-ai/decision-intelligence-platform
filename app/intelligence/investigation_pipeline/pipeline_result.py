"""
Sentinel DNA
Pipeline Result

Represents the final output of an investigation pipeline.
"""


class PipelineResult:

    def __init__(
        self,
        investigation_id,
        status="pending",
        findings=None,
        results=None,
    ):

        self.investigation_id = investigation_id

        self.status = status

        self.findings = findings or []

        self.results = results or []


    def add_result(
        self,
        result,
    ):

        self.results.append(result)


    def add_finding(
        self,
        finding,
    ):

        self.findings.append(finding)


    def complete(self):

        self.status = "completed"


    def fail(self):

        self.status = "failed"


    def to_dict(self):

        return {

            "investigation_id":
                self.investigation_id,

            "status":
                self.status,

            "findings":
                self.findings,

            "results":
                self.results,

        }