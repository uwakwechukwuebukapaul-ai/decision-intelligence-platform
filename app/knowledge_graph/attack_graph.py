class AttackGraph:


    def analyze(self, relationships):


        paths = []


        for relation in relationships:

            paths.append(
                {
                    "from":
                    relation["source"],

                    "to":
                    relation["target"],

                    "risk":
                    "potential_attack_path"
                }
            )


        return paths