from app.intelligence.pipeline.intelligence_pipeline import IntelligencePipeline
from app.intelligence.pipeline.pipeline_result import PipelineResult
from app.intelligence.pipeline.pipeline_stage import PipelineStage


class SuccessStage(PipelineStage):

    def __init__(self):
        super().__init__("success")
    @property
    def name(self) -> str:
        return "success"

    def execute(self, context):
        updated = dict(context)
        updated["executed"] = updated.get("executed", 0) + 1

        return PipelineResult.success_result(
            stage=self.name,
            context=updated,
        )


class FailureStage(PipelineStage):

    def __init__(self):
        super().__init__("failure")
    @property
    def name(self) -> str:
        return "failure"

    def execute(self, context):
        return PipelineResult.failure_result(
            stage=self.name,
            context=context,
            message="Stage failed.",
        )


def test_register_stage():

    pipeline = IntelligencePipeline()

    pipeline.register_stage(SuccessStage())

    assert len(pipeline.stages) == 1


def test_pipeline_success():

    pipeline = IntelligencePipeline()

    pipeline.register_stage(SuccessStage())
    pipeline.register_stage(SuccessStage())

    result = pipeline.execute({})

    assert result.success
    assert result.context["executed"] == 2


def test_pipeline_fail_fast():

    pipeline = IntelligencePipeline()

    pipeline.register_stage(SuccessStage())
    pipeline.register_stage(FailureStage())
    pipeline.register_stage(SuccessStage())

    result = pipeline.execute({})

    assert not result.success
    assert result.stage == "failure"


def test_empty_pipeline_returns_success():

    pipeline = IntelligencePipeline()

    result = pipeline.execute({})

    assert result.success