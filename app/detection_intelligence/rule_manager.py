from datetime import datetime
import uuid


class RuleManager:


    def __init__(self):

        self.rules = {}



    def create_rule(
        self,
        name,
        pattern,
        severity="medium",
        mitre_techniques=None
    ):

        rule_id = (
            f"RULE-{uuid.uuid4().hex[:8].upper()}"
        )

        rule = {

            "rule_id": rule_id,

            "name": name,

            "pattern": pattern,

            "severity": severity,

            "mitre_techniques": mitre_techniques or [],

            "enabled": True,

            "created_at": datetime.utcnow().isoformat()

        }


        self.rules[rule_id] = rule


        return rule



    def enable_rule(
        self,
        rule_id
    ):

        if rule_id in self.rules:

            self.rules[rule_id]["enabled"] = True

        return self.rules.get(rule_id)



    def disable_rule(
        self,
        rule_id
    ):

        if rule_id in self.rules:

            self.rules[rule_id]["enabled"] = False

        return self.rules.get(rule_id)



    def list_rules(self):

        return list(
            self.rules.values()
        )