from datetime import datetime


class PipelineValidator:


    def validate(self, pipeline):


        required = [

            "research",

            "prediction",

            "planning",

            "execution",

            "investment",

            "executive"

        ]


        missing = [

            item for item in required
            if item not in pipeline

        ]


        return {


            "valid":
                len(missing) == 0,


            "missing":

                missing,


            "timestamp":

                datetime.utcnow().isoformat()

        }