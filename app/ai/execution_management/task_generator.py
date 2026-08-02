from datetime import datetime



class TaskGenerator:
    """
    Generates executable tasks from strategic objectives.
    """



    def __init__(self):

        self.version = "1.0"



    def generate_tasks(self, user_id):


        tasks = [

            "Analyze current cybersecurity capability",

            "Complete security engineering learning objectives",

            "Build practical cybersecurity projects",

            "Improve enterprise security knowledge",

            "Evaluate career progression performance"

        ]


        return {


            "user_id":

                user_id,


            "tasks":

                [

                    {

                        "task_id":

                            index + 1,


                        "task":

                            task,


                        "status":

                            "created"

                    }

                    for index, task in enumerate(tasks)

                ],



            "task_count":

                len(tasks),



            "task_status":

                "generated",



            "generated_at":

                datetime.utcnow().isoformat(),



            "version":

                self.version

        }