from app.ai.memory.memory_engine import MemoryEngine
from app.ai.learning.pattern_analyzer import PatternAnalyzer
from app.ai.learning.improvement_engine import ImprovementEngine



class LearningEngine:


    def __init__(self):

        self.memory = MemoryEngine()

        self.patterns = PatternAnalyzer()

        self.improver = ImprovementEngine()



    def learn(
        self,
        agent_id
    ):


        context = self.memory.recall(
            agent_id
        )


        analysis = self.patterns.analyze(
            context["memories"]
        )


        improvement = self.improver.generate_improvement(
            analysis["patterns"]
        )


        return {

            "agent_id":
                agent_id,

            "analysis":
                analysis,

            "improvement":
                improvement

        }