class CapabilityManager:


    def upgrade(
        self,
        capabilities,
        improvements
    ):


        updated = list(
            capabilities
        )


        for item in improvements:

            capability = item.lower().replace(
                " ",
                "_"
            )


            if capability not in updated:

                updated.append(
                    capability
                )


        return updated