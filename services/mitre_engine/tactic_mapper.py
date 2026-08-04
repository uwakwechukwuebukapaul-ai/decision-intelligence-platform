class TacticMapper:



    def map(self, techniques):

        tactics = []


        for technique in techniques:

            tactic = technique["tactic"]

            if tactic not in tactics:

                tactics.append(
                    tactic
                )


        return tactics