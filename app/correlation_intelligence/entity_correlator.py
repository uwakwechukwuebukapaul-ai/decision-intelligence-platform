class EntityCorrelator:


    def correlate(self, data):

        entities = []

        relationships = []


        if data.get("indicator"):

            entities.append(data["indicator"])

            relationships.append(
                "IOC linked to investigation"
            )


        if data.get("asset"):

            entities.append(data["asset"])

            relationships.append(
                "Threat associated with asset"
            )


        if data.get("identity"):

            entities.append(data["identity"])

            relationships.append(
                "Identity involved in activity"
            )


        if data.get("vulnerability"):

            entities.append(data["vulnerability"])

            relationships.append(
                "Asset affected by vulnerability"
            )


        return {
            "entities": entities,
            "relationships": relationships
        }