class IntelligenceMerger:
    """
    Merges intelligence outputs from multiple engines.
    """

    def merge(
        self,
        evidence=None,
        detection=None,
        threat=None,
        hunting=None,
        knowledge=None,
        cognitive=None
    ):

        return {

            "evidence": evidence or {},

            "detection": detection or {},

            "threat_intelligence": threat or {},

            "threat_hunting": hunting or {},

            "knowledge_graph": knowledge or {},

            "cognitive_analysis": cognitive or {}

        }