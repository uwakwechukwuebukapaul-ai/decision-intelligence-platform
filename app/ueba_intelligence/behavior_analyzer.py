class BehaviorAnalyzer:


    def analyze(
        self,
        user,
        activity
    ):

        profile = {

            "user": user,

            "activity": activity,

            "normal": True

        }


        if "new_location" in activity:

            profile["normal"] = False


        return profile