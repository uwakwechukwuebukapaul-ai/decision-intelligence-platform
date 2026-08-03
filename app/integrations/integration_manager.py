from datetime import datetime

from app.integrations.siem_connector import SIEMConnector
from app.integrations.edr_connector import EDRConnector
from app.integrations.threat_intel_connector import ThreatIntelConnector
from app.integrations.cloud_connector import CloudConnector
from app.integrations.ticketing_connector import TicketingConnector
from app.integrations.integration_memory import IntegrationMemory



class IntegrationManager:



    def __init__(self):

        self.siem = SIEMConnector()

        self.edr = EDRConnector()

        self.threat_intel = ThreatIntelConnector()

        self.cloud = CloudConnector()

        self.ticketing = TicketingConnector()

        self.memory = IntegrationMemory()



    def connect_all(self, platform):


        result = {


            "platform":

                platform,



            "integrations":

                {


                    "SIEM":

                        self.siem.connect(
                            "Microsoft Sentinel"
                        ),



                    "EDR":

                        self.edr.connect(
                            "CrowdStrike Falcon"
                        ),



                    "Threat Intelligence":

                        self.threat_intel.connect(
                            "Threat Intelligence Feeds"
                        ),



                    "Cloud":

                        self.cloud.connect(
                            "Azure"
                        ),



                    "Ticketing":

                        self.ticketing.connect(
                            "ServiceNow"
                        )

                },



            "timestamp":

                datetime.utcnow().isoformat()

        }



        self.memory.store(result)



        return {


            "status":

                "completed",



            "integration_gateway":

                result

        }