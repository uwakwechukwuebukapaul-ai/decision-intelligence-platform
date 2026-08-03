import os


class ConfigManager:


    def load(self):

        return {

            "environment":
                os.getenv(
                    "ENVIRONMENT",
                    "development"
                ),

            "database":
                os.getenv(
                    "DATABASE",
                    "sentinel.db"
                ),

            "security_mode":
                "enabled",

            "logging":
                "enabled"
        }