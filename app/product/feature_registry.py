class FeatureRegistry:


    def __init__(self):

        self.features = [

            {
                "name":
                    "AI SOC Investigation Copilot",

                "category":
                    "Investigation",

                "value":
                    "Autonomous security investigation assistance"
            },


            {
                "name":
                    "Alert Triage Engine",

                "category":
                    "Detection",

                "value":
                    "Prioritizes alerts using AI reasoning"
            },


            {
                "name":
                    "Threat Intelligence Engine",

                "category":
                    "Threat Intelligence",

                "value":
                    "IOC enrichment and threat analysis"
            },


            {
                "name":
                    "MITRE ATT&CK Mapper",

                "category":
                    "Threat Analysis",

                "value":
                    "Maps incidents to adversary techniques"
            },


            {
                "name":
                    "SOAR Automation",

                "category":
                    "Automation",

                "value":
                    "Automates security response workflows"
            },


            {
                "name":
                    "AI Security Memory",

                "category":
                    "Learning",

                "value":
                    "Continuous investigation knowledge retention"
            }

        ]



    def list_features(self):

        return {

            "count":
                len(self.features),

            "features":
                self.features

        }