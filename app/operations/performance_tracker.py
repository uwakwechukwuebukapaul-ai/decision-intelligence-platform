from datetime import datetime


class PerformanceTracker:



    def __init__(self):

        self.metrics = []



    def record(

        self,

        operation,

        execution_time

    ):


        event = {


            "operation":

                operation,


            "execution_time_ms":

                execution_time,


            "timestamp":

                datetime.utcnow().isoformat()

        }



        self.metrics.append(event)


        return event



    def report(self):


        return {


            "total_operations":

                len(self.metrics),


            "performance":

                self.metrics

        }