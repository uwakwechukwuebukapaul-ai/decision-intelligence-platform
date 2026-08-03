class PatternAnalyzer:


    def analyze(self, memories):

        patterns = []


        for memory in memories:

            content = memory.get(
                "content",
                ""
            ).lower()


            if "ai" in content:
                patterns.append(
                    "Artificial intelligence trend detected"
                )


            if "security" in content:
                patterns.append(
                    "Security intelligence trend detected"
                )


            if "market" in content:
                patterns.append(
                    "Market analysis pattern detected"
                )


        return {

            "patterns": list(
                set(patterns)
            ),

            "memory_count":
                len(memories)

        }