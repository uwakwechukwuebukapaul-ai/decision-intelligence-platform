from datetime import datetime


from .event_ingestion import EventIngestion
from .log_pipeline import LogPipeline
from .schema_normalizer import SchemaNormalizer
from .data_lake import DataLake
from .search_engine import SearchEngine
from .analytics_engine import AnalyticsEngine
from .data_memory import DataMemory



class DataEngine:
    """
    Sentinel DNA Enterprise Data Intelligence Engine.
    """


    def __init__(self):

        self.ingestion = EventIngestion()

        self.pipeline = LogPipeline()

        self.normalizer = SchemaNormalizer()

        self.data_lake = DataLake()

        self.search = SearchEngine()

        self.analytics = AnalyticsEngine()

        self.memory = DataMemory()



    def process(
        self,
        source,
        event
    ):


        ingested = self.ingestion.ingest(
            source,
            event
        )


        normalized = self.normalizer.normalize(
            ingested
        )


        processed = self.pipeline.process(
            normalized
        )


        stored = self.data_lake.store(
            normalized
        )


        self.memory.store(
            normalized
        )


        analytics = self.analytics.analyze(
            self.memory.get_all()["events"]
        )


        return {


            "status":
                "completed",


            "ingestion":
                ingested,


            "normalization":
                normalized,


            "pipeline":
                processed,


            "storage":
                stored,


            "analytics":
                analytics,


            "created_at":
                datetime.utcnow().isoformat()

        }