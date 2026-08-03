from datetime import datetime


class AttackNavigator:


    def build(self, techniques):

        layers = []


        for technique in techniques["techniques"]:

            layers.append({
                "technique_id": technique["id"],
                "technique": technique["name"],
                "enabled": True
            })


        return {
            "navigator_layer": {
                "name": "Sentinel DNA ATT&CK Layer",
                "techniques": layers
            },
            "timestamp": datetime.now().isoformat()
        }