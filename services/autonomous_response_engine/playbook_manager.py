class PlaybookManager:
    """
    SOAR playbook management.
    """

    def __init__(self):

        self.playbooks = []


    def create_playbook(self, name, actions):

        playbook = {
            "name": name,
            "actions": actions
        }

        self.playbooks.append(playbook)

        return playbook


    def get_playbooks(self):

        return self.playbooks