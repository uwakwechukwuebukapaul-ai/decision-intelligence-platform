from datetime import datetime

from .hypothesis_generator import HypothesisGenerator
from .query_generator import QueryGenerator
from .attack_mapper import AttackMapper
from .behavior_hunter import BehaviorHunter
from .ioc_hunter import IOCHunter
from .investigation_tracker import InvestigationTracker


class HuntEngine:


    def __init__(self):

        self.hypothesis = HypothesisGenerator()
        self.query = QueryGenerator()
        self.attack = AttackMapper()
        self.behavior = BehaviorHunter()
        self.ioc = IOCHunter()
        self.tracker = InvestigationTracker()



    def hunt(self, intelligence):


        hypothesis = self.hypothesis.generate(
            intelligence
        )


        queries = self.query.generate(
            intelligence
        )


        attack = self.attack.map(
            intelligence
        )


        behavior = self.behavior.search(
            intelligence
        )


        iocs = self.ioc.search(
            intelligence
        )


        investigation = self.tracker.create(
            intelligence
        )


        return {

            "status": "completed",

            "hunt_input": intelligence,

            "hypothesis": hypothesis,

            "queries": queries,

            "mitre_mapping": attack,

            "behavior_findings": behavior,

            "ioc_findings": iocs,

            "investigation": investigation,

            "created_at":
                datetime.utcnow().isoformat()

        }