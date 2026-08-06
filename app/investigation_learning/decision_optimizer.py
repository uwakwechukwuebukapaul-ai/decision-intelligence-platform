class DecisionOptimizer:

    def optimize(self, previous_decision, confidence, patterns):

        if confidence >= 0.85:
            optimized = previous_decision
            improvement = "Decision confidence reinforced"

        elif patterns:
            optimized = "investigate"
            improvement = "Decision upgraded using threat patterns"

        else:
            optimized = "monitor"
            improvement = "Reduced response priority"

        return {
            "optimized_decision": optimized,
            "improvement": improvement
        }