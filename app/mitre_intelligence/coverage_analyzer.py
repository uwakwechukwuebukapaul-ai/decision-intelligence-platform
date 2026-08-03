from datetime import datetime


class CoverageAnalyzer:


    def analyze(self, techniques):

        return {

            "coverage":

            [

                {
                    "technique":
                        technique["name"],

                    "detection_available":
                        True,

                    "coverage_score":
                        85

                }

                for technique in techniques["techniques"]

            ],

            "timestamp":
                datetime.utcnow().isoformat()
        }