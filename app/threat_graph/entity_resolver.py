class EntityResolver:


    def resolve(self, event):

        entities = []


        keywords = {
            "ransomware": "Malware",
            "powershell": "Technique",
            "finance": "Asset",
            "server": "Infrastructure",
            "actor": "Threat Actor"
        }


        text = event.lower()


        for key, value in keywords.items():

            if key in text:

                entities.append(
                    {
                        "entity": key,
                        "type": value
                    }
                )


        return {
            "entities": entities,
            "count": len(entities)
        }