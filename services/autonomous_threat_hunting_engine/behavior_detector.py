class BehaviorDetector:

    def analyze(self, activity):

        return {
            "activity": activity,
            "behavior": "analyzed"
        }


    def detect_ttp(self, behavior):

        return {
            "techniques": []
        }