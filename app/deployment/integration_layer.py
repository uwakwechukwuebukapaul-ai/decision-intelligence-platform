class IntegrationLayer:



    def integrations(self):


        return {


            "supported_integrations": [


                {

                    "category":
                        "SIEM",

                    "examples":
                        [

                            "Microsoft Sentinel",

                            "Splunk",

                            "Elastic Security",

                            "Google SecOps"

                        ]

                },


                {


                    "category":
                        "EDR/XDR",

                    "examples":

                        [

                            "CrowdStrike",

                            "Cortex XDR",

                            "Defender"

                        ]

                },


                {


                    "category":
                        "Threat Intelligence",

                    "examples":

                        [

                            "IOC feeds",

                            "MITRE ATT&CK",

                            "OSINT sources"

                        ]

                }


            ]

        }