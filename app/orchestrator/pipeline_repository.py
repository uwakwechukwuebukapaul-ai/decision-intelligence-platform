from datetime import datetime


class PipelineRepository:

    def __init__(self):
        self.executions = []

    def save(self, pipeline_result):
        record = pipeline_result.to_dict()
        self.executions.append(record)
        return record

    def get_all(self):
        return self.executions