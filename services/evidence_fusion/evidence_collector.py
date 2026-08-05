from .evidence_model import Evidence



class EvidenceCollector:
    """
    Collects and normalizes investigation evidence.
    """


    def __init__(self):

        self.evidence = []



    def collect(
        self,
        evidence_type,
        data,
        source
    ):


        item = Evidence(

            evidence_type,

            data,

            source

        )


        self.evidence.append(item)


        return item



    def all(
        self
    ):

        return [

            item.to_dict()

            for item in self.evidence

        ]