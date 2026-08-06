"""
Sentinel DNA Database Migrations

Safe SQLite schema upgrades.
"""


from .db import Database




class DatabaseMigration:
    """
    Handles incremental database upgrades.
    """



    def __init__(self):

        self.db = Database()



    def migrate(self):

        self.ensure_timeline_schema()



    def ensure_timeline_schema(self):

        tables = self.get_tables()


        if "timeline_events" not in tables:

            return



        columns = self.get_columns(
            "timeline_events"
        )



        required_columns = {

            "event_id": "TEXT",

            "incident_id": "TEXT",

            "stage": "TEXT",

            "message": "TEXT",

            "created_at": "TEXT",

        }



        for column, data_type in required_columns.items():

            if column not in columns:

                self.db.execute(

                    f"""
                    ALTER TABLE timeline_events
                    ADD COLUMN {column} {data_type}
                    """

                )



    def get_tables(self):

        rows = self.db.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        )


        tables = []


        for row in rows:

            try:
                tables.append(row["name"])

            except:

                tables.append(row[0])


        return tables



    def get_columns(
        self,
        table_name,
    ):

        rows = self.db.execute(

            f"""
            PRAGMA table_info({table_name})
            """

        )


        columns = []


        for row in rows:

            try:
                columns.append(row["name"])

            except:

                columns.append(row[1])


        return columns