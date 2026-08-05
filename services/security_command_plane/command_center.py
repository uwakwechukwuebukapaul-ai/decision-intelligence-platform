class CommandCenter:
    """
    Central command interface for Sentinel DNA.
    """

    def __init__(self):
        self.commands = []

    def execute(self, command, payload=None):

        record = {
            "command": command,
            "payload": payload,
            "status": "executed"
        }

        self.commands.append(record)

        return record


    def history(self):
        return self.commands