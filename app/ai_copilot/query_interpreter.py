from datetime import datetime


class QueryInterpreter:
    """
    Understands analyst security questions.
    """


    def interpret(
        self,
        query
    ):

        intent = "general_security_analysis"


        if "investigate" in query.lower():

            intent = "investigation"


        elif "respond" in query.lower():

            intent = "incident_response"


        elif "detect" in query.lower():

            intent = "threat_detection"



        return {

            "query":
                query,

            "intent":
                intent,

            "timestamp":
                datetime.utcnow().isoformat()

        }