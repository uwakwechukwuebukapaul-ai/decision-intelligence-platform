from .event_normalizer import EventNormalizer
from .schema_mapper import SchemaMapper


class IngestionPipeline:
    """
    Complete ingestion workflow.
    """

    def __init__(self):

        self.normalizer = EventNormalizer()
        self.mapper = SchemaMapper()


    def process(self, event):

        normalized = self.normalizer.normalize(event)

        mapped = self.mapper.map(normalized)

        return {
            "status": "processed",
            "event": mapped
        }