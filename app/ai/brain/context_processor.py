from datetime import datetime


class ContextProcessor:


    def process(

        self,

        mission,

        memories=None

    ):


        return {

            "mission":
                mission,


            "memory_context":
                memories or [],


            "context_ready":
                True,


            "timestamp":
                datetime.utcnow().isoformat()

        }