from .graph_model import GraphEntity


class EntityEngine:
    """
    Extracts security intelligence entities.
    """


    def extract(
        self,
        text
    ):

        entities = []

        lowered = text.lower()



        patterns = {


            "powershell":
                "Technique",


            "ransomware":
                "Malware",


            "apt":
                "Threat Actor",


            "cve":
                "Vulnerability",


            "phishing":
                "Attack Vector",


            "database":
                "Target Asset"

        }



        for keyword, entity_type in patterns.items():

            if keyword in lowered:

                entities.append(

                    GraphEntity(

                        name=keyword,

                        entity_type=entity_type,

                        attributes={
                            "source": "analysis_engine"
                        }

                    )

                )


        return entities