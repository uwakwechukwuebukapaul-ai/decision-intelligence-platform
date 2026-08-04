class TechniqueMapper:


    def __init__(self, database):

        self.database = database



    def map(self, event):

        matches = []

        text = event.lower()


        for keyword in self.database.techniques:

            if keyword in text:

                technique = self.database.search(
                    keyword
                )

                matches.append(
                    technique
                )


        return matches