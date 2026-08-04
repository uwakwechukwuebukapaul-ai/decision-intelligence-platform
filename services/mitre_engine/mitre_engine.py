from .attack_database import AttackDatabase
from .technique_mapper import TechniqueMapper
from .tactic_mapper import TacticMapper
from .mitre_logger import MitreLogger



class MitreEngine:



    def __init__(self):

        self.database = AttackDatabase()

        self.technique_mapper = TechniqueMapper(
            self.database
        )

        self.tactic_mapper = TacticMapper()

        self.logger = MitreLogger()



    def analyze(self, event):


        techniques = self.technique_mapper.map(
            event
        )


        tactics = self.tactic_mapper.map(
            techniques
        )


        return {

            "event": event,

            "techniques": techniques,

            "tactics": tactics,

            "status":
                "mitre_mapped",

            "log":
                self.logger.log(
                    "MITRE analysis completed"
                )

        }