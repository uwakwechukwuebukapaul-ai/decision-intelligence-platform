from datetime import datetime


class CoverageAnalyzer:


    def analyze(self, techniques):

        covered = len(
            techniques["techniques"]
        )


        gaps = []


        if covered < 3:
            gaps.append(
                "Additional ATT&CK coverage recommended"
            )


        return {
            "coverage_score": covered * 30,
            "covered_techniques": covered,
            "gaps": gaps,
            "timestamp": datetime.now().isoformat()
        }