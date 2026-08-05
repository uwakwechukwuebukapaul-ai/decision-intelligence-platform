class RuleValidator:
    """
    Validates generated detection rules.
    """


    def validate(
        self,
        rule
    ):


        required = [

            "name",

            "severity",

            "logic"

        ]


        valid = all(

            field in rule

            for field in required

        )


        return {

            "valid":
                valid,


            "issues":
                []

                if valid

                else
                [
                    "missing detection fields"
                ]

        }