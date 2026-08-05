class AnalystLearning:

    def __init__(self):
        self.lessons = []

    def learn(self, lesson):
        self.lessons.append(lesson)
        return lesson

    def knowledge(self):
        return self.lessons