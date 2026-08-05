from datetime import datetime


class ModelImprovement:
    """
    Handles AI model improvement lifecycle.
    """

    def __init__(self):
        self.improvements = []

    def propose_update(self, model, reason):
        update = {
            "model": model,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "proposed"
        }

        self.improvements.append(update)

        return update

    def approve_update(self, model):
        for item in self.improvements:
            if item["model"] == model:
                item["status"] = "approved"

        return True

    def history(self):
        return self.improvements