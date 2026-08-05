class DependencyRegistry:

    def __init__(self):
        self.dependencies = {}

    def add_dependency(self, name, dependency):
        self.dependencies[name] = dependency

    def resolve(self, name):
        return self.dependencies.get(name)

    def list_dependencies(self):
        return list(self.dependencies.keys())