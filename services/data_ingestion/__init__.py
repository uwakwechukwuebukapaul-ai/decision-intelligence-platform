from .ingestion_engine import IngestionEngine
from .event_normalizer import EventNormalizer
from .log_parser import LogParser
from .telemetry_processor import TelemetryProcessor
from .alert_ingestor import AlertIngestor
from .schema_mapper import SchemaMapper
from .ingestion_pipeline import IngestionPipeline


class DataIngestion:

    def __init__(self):
        self.pipeline = IngestionPipeline()
        self.engine = IngestionEngine()

        self.components = {
            "normalizer": EventNormalizer(),
            "parser": LogParser(),
            "telemetry": TelemetryProcessor(),
            "alert_ingestor": AlertIngestor(),
            "schema_mapper": SchemaMapper()
        }

    def ingest(self, data):
        return self.pipeline.process(data)

    def status(self):
        return {
            "service": "Data Ingestion",
            "components": list(self.components.keys()),
            "status": "ready"
        }