class DataLifecycle:
    """
    Security data lifecycle management layer.

    Responsible for:
    - ingestion tracking
    - archival decisions
    - retention workflow
    - deletion lifecycle states
    """

    def __init__(self):

        self.lifecycle_records = []


    def register_data(self, data_id, data_type):

        record = {
            "data_id": data_id,
            "data_type": data_type,
            "state": "active"
        }

        self.lifecycle_records.append(record)

        return record


    def update_state(self, data_id, state):

        for record in self.lifecycle_records:

            if record["data_id"] == data_id:

                record["state"] = state

                return record

        return None


    def get_state(self, data_id):

        for record in self.lifecycle_records:

            if record["data_id"] == data_id:

                return record["state"]

        return None


    def list_records(self):

        return self.lifecycle_records


    def archive(self, data_id):

        return self.update_state(data_id, "archived")


    def delete(self, data_id):

        return self.update_state(data_id, "deleted")