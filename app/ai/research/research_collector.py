from datetime import datetime


class ResearchCollector:


    def collect(self, question):

        evidence = []


        if "AI SOC" in question.upper():

            evidence.extend([

                "SOC teams experience alert overload",

                "Security analysts spend significant time on investigation tasks",

                "AI automation can reduce repetitive security operations work",

                "Organizations are increasing cybersecurity automation investment"

            ])


        else:

            evidence.append(
                "General intelligence research collected"
            )


        return {

            "question": question,

            "evidence": evidence,

            "collected_at":
                datetime.utcnow().isoformat()

        }