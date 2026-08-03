from datetime import datetime


class ExecutionMonitor:


    def monitor(
        self,
        execution_results
    ):

        total = execution_results.get(
            "executed",
            0
        )


        return {

            "execution_count":
                total,

            "health":
                "optimal" if total > 0 else "empty",

            "timestamp":
                datetime.utcnow().isoformat()

        }