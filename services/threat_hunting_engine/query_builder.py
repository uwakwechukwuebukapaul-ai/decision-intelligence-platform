class QueryBuilder:
    """
    Builds platform-independent hunting queries.
    """

    def build(self, hunt):

        objective = hunt["objective"].lower()


        query = {

            "data_source":
            "security_events",

            "filters": []

        }


        if "powershell" in objective:

            query["filters"].append(
                "process_name=powershell.exe"
            )


        if "ransomware" in objective:

            query["filters"].append(
                "file_encryption_activity=true"
            )


        if "credential" in objective:

            query["filters"].append(
                "credential_access_events=true"
            )


        if "lateral" in objective:

            query["filters"].append(
                "remote_connection_activity=true"
            )


        return query