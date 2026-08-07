"""
Default Sentinel DNA Intelligence Engines
"""



class RiskEngine:


    def execute(
        self,
        payload,
        context=None,
    ):

        score = 30


        if context:

            if len(context.iocs) > 0:

                score += 40


            if len(context.evidence) > 0:

                score += 20



        return {

            "risk_score": score,

            "case_id":
                context.case_id
                if context else None

        }




class ThreatClassifier:


    def execute(
        self,
        payload,
        context=None,
    ):

        return {

            "classification":
                "malicious",

            "ioc_count":
                len(context.iocs)
                if context else 0

        }




class MitreEngine:


    def execute(
        self,
        payload,
        context=None,
    ):

        return {

            "techniques":[
                "T1566"
            ],

            "evidence_reviewed":
                len(context.evidence)
                if context else 0

        }




class IOCEnrichmentEngine:


    def execute(
        self,
        payload,
        context=None,
    ):

        return {

            "ioc_count":
                len(context.iocs)
                if context else 0

        }




def load_default_engines():

    return {

        "risk_scoring":
            RiskEngine(),

        "threat_classification":
            ThreatClassifier(),

        "mitre_mapping":
            MitreEngine(),

        "ioc_enrichment":
            IOCEnrichmentEngine(),

    }