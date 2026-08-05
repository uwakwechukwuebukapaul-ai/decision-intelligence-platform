class InvestigationPlan:
    """
    Creates autonomous investigation workflow.
    """

    def create(
        self,
        hypotheses
    ):

        steps = []


        for hypothesis in hypotheses:

            steps.append({

                "step": len(steps)+1,

                "action":
                "Collect evidence for " +
                hypothesis["hypothesis"],

                "confidence":
                hypothesis["confidence"]

            })


        steps.extend([

            {
                "step": len(steps)+1,
                "action": "Map activity to MITRE ATT&CK techniques"
            },

            {
                "step": len(steps)+1,
                "action": "Generate analyst recommendation"
            }

        ])


        return {

            "investigation_steps": steps

        }