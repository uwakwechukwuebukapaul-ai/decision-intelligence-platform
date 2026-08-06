from .query_builder import QueryBuilder
from .hypothesis_engine import HypothesisEngine
from .hunt_repository import HuntRepository
from .hunt_schema import create_hunt



class HuntEngine:


    def __init__(self):

        self.query_builder = QueryBuilder()

        self.hypothesis_engine = HypothesisEngine()

        self.repository = HuntRepository()



    def create_hunt(
        self,
        indicator
    ):

        hypothesis = self.hypothesis_engine.generate(
            indicator
        )


        queries = self.query_builder.build_queries(
            indicator
        )


        hunt = create_hunt(

            indicator,

            hypothesis["hypothesis"],

            queries,

            hypothesis["mitre_mapping"]

        )


        return self.repository.save(
            hunt
        )



    def get_hunts(self):

        return self.repository.get_all()