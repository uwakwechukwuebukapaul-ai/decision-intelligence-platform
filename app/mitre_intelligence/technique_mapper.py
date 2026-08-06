class TechniqueMapper:


    def map(self, context):

        techniques = []


        indicator = context.get("indicator")

        identity = context.get("identity")


        if indicator:

            techniques.append(
                "T1105 Ingress Tool Transfer"
            )


            techniques.append(
                "T1071 Application Layer Protocol"
            )


        if identity:

            techniques.append(
                "T1078 Valid Accounts"
            )


        if context.get("asset"):

            techniques.append(
                "T1190 Exploit Public-Facing Application"
            )


        return techniques