def adjust_confidence(score):

    if score >= 90:

        return {

            "confidence":
                "high",

            "adjustment":
                "increase future trust weighting"

        }


    return {

        "confidence":
            "medium",

        "adjustment":
            "monitor future decisions"

    }