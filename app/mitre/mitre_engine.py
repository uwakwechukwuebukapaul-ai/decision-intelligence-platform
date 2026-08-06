from .technique_mapper import TechniqueMapper
from .tactic_mapper import TacticMapper
from .mitre_repository import MITRERepository
from .mitre_schema import create_mapping


class MITREEngine:

    def __init__(self):

        self.techniques = TechniqueMapper()

        self.tactics = TacticMapper()

        self.repository = MITRERepository()

    def map_technique(self, indicator):

        technique = self.techniques.map(
            indicator
        )

        tactic = self.tactics.map(
            technique["technique"]
        )

        mapping = create_mapping(

            indicator=indicator,

            technique=technique["technique"],

            tactic=tactic,

            name=technique["name"],

            confidence=technique["confidence"],

        )

        return self.repository.save(
            mapping
        )

    def get_all(self):

        return self.repository.get_all()