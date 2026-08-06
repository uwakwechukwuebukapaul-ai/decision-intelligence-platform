from app.intelligence.pipeline.pipeline_result import PipelineResult
from app.intelligence.pipeline.pipeline_stage import PipelineStage
from app.intelligence.pipeline.stage_executor import StageExecutor


class SuccessStage(PipelineStage):

    def __init__(self):
        super().__init__("success")
   

    def execute(self, context):
        updated = dict(context)
        updated["count"] = updated.get("count", 0) + 1

        return PipelineResult.success_result(
            stage=self.name,
            context=updated,
        )


class ExceptionStage(PipelineStage):

    def __init__(self):
        super().__init__("exception")
    

    def execute(self, context):
        raise RuntimeError("Unexpected failure")


def test_executor_runs_stage():

    executor = StageExecutor()

    result = executor.execute(
        SuccessStage(),
        {},
    )

    assert result.success
    assert result.context["count"] == 1


def test_executor_preserves_context():

    executor = StageExecutor()

    result = executor.execute(
        SuccessStage(),
        {"user": "analyst"},
    )

    assert result.success
    assert result.context["user"] == "analyst"
    assert result.context["count"] == 1


def test_executor_handles_exception():

    executor = StageExecutor()

    result = executor.execute(
        ExceptionStage(),
        {},
    )

    assert not result.success
    assert result.stage == "exception"
    assert "Unexpected failure" in result.message