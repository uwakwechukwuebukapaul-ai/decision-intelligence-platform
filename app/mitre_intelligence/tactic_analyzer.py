class TacticAnalyzer:


    def analyze(self, techniques):

        tactics = []


        for technique in techniques:


            if "T1105" in technique:

                tactics.append(
                    "Command and Control"
                )


            if "T1071" in technique:

                tactics.append(
                    "Command and Control"
                )


            if "T1078" in technique:

                tactics.append(
                    "Credential Access"
                )


            if "T1190" in technique:

                tactics.append(
                    "Initial Access"
                )


        return list(set(tactics))