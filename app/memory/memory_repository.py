from datetime import datetime
import uuid



class MemoryRepository:


    def __init__(self):

        self.storage = {}



    def save(
        self,
        category,
        data
    ):


        memory_id = (

            "MEM-"
            +
            uuid.uuid4().hex[:8].upper()

        )


        self.storage[memory_id] = {


            "memory_id":
                memory_id,


            "category":
                category,


            "data":
                data,


            "created_at":
                datetime.utcnow().isoformat()

        }


        return self.storage[memory_id]



    def get(
        self,
        category=None
    ):


        memories = list(
            self.storage.values()
        )


        if category:

            memories = [

                m for m in memories

                if m["category"] == category

            ]


        return memories