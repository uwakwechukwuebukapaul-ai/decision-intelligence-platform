class ContextManager:

    def build(self, event):

        return {
            "event": event,
            "entities": self.extract_entities(event),
            "metadata": {
                "source": "sentinel_dna"
            }
        }


    def extract_entities(self, event):

        entities = []

        if isinstance(event, dict):

            for key, value in event.items():

                entities.append(
                    {
                        "type": key,
                        "value": value
                    }
                )

        return entities