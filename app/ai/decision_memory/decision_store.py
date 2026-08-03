from datetime import datetime
import uuid


class DecisionStore:
    """
    Persistent Decision Memory Layer

    Stores:
    - Historical decisions
    - Reasoning context
    - Confidence levels
    - Outcomes
    - Success patterns
    """


    def __init__(self):

        self.decisions = []


    def save_decision(
        self,
        agent_id,
        mission,
        reasoning,
        decision,
        confidence
    ):

        record = {

            "decision_id":
                f"DEC-{uuid.uuid4().hex[:8].upper()}",


            "agent_id":
                agent_id,


            "mission":
                mission,


            "reasoning":
                reasoning,


            "decision":
                decision,


            "confidence":
                confidence,


            "outcome":
                None,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.decisions.append(record)


        return {

            "status":
                "stored",

            "decision":
                record

        }



    def update_outcome(
        self,
        decision_id,
        outcome
    ):


        for decision in self.decisions:


            if decision["decision_id"] == decision_id:


                decision["outcome"] = outcome


                decision["updated_at"] = (
                    datetime.utcnow().isoformat()
                )


                return {


                    "status":
                        "updated",


                    "decision":
                        decision

                }



        return {


            "status":
                "not_found"

        }



    def get_decisions(
        self,
        agent_id=None
    ):


        if agent_id:


            results = [

                decision

                for decision in self.decisions

                if decision["agent_id"] == agent_id

            ]


        else:


            results = self.decisions



        return {


            "count":
                len(results),


            "decisions":
                results

        }



    def search(
        self,
        keyword
    ):


        results = []


        keyword = keyword.lower()



        for decision in self.decisions:


            searchable = str(
                decision
            ).lower()



            if keyword in searchable:


                results.append(
                    decision
                )



        return {


            "count":
                len(results),


            "results":
                results

        }



    def get_success_patterns(self):


        successful = []


        for decision in self.decisions:


            if decision.get(
                "outcome"
            ) == "success":


                successful.append(
                    {

                        "mission":
                            decision["mission"],


                        "decision":
                            decision["decision"],


                        "confidence":
                            decision["confidence"]

                    }
                )



        return {


            "successful_decisions":
                len(successful),


            "patterns":
                successful

        }



    def memory_summary(self):


        return {


            "total_decisions":
                len(self.decisions),


            "success_patterns":
                self.get_success_patterns(),


            "timestamp":
                datetime.utcnow().isoformat()

        }