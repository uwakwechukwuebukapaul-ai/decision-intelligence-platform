from datetime import datetime

from .log_collector import LogCollector
from .event_normalizer import EventNormalizer
from .schema_mapper import SchemaMapper
from .siem_connector import SIEMConnector
from .endpoint_connector import EndpointConnector
from .cloud_connector import CloudConnector
from .network_connector import NetworkConnector
from .ingestion_memory import IngestionMemory
from .ingestion_logger import IngestionLogger


class EventIngestionEngine:

    def __init__(self):

        self.collector = LogCollector()
        self.normalizer = EventNormalizer()
        self.mapper = SchemaMapper()

        self.siem = SIEMConnector()
        self.endpoint = EndpointConnector()
        self.cloud = CloudConnector()
        self.network = NetworkConnector()

        self.memory = IngestionMemory()
        self.logger = IngestionLogger()


    def ingest(self, event):

        collected = self.collector.collect(event)

        normalized = self.normalizer.normalize(
            collected
        )

        mapped = self.mapper.map(
            normalized
        )

        sources = {
            "siem": self.siem.connect(),
            "endpoint": self.endpoint.connect(),
            "cloud": self.cloud.connect(),
            "network": self.network.connect()
        }

        memory = self.memory.store(
            event
        )

        log = self.logger.record(
            event
        )


        return {

            "status": "completed",

            "event": event,

            "collection": collected,

            "normalization": normalized,

            "schema_mapping": mapped,

            "connectors": sources,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.utcnow().isoformat()

        }