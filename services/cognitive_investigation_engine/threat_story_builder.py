class ThreatStoryBuilder:


    def build(
        self,
        case,
        evidence,
        attack_path,
        techniques
    ):

        return {
            "summary":
                "Threat investigation narrative generated",

            "case": case,

            "evidence_summary": evidence,

            "attack_summary": attack_path,

            "techniques": techniques
        }